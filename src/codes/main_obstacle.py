'''
This is a very basic program that uses DonkeyCar camera images to feed a Keras model to make predictions.
'''

import os
import time
import sys
current_path = os.getcwd()
sys.path.append(current_path)
from donkeycar.parts.camera import PiCamera  # Import the PiCamera class from DonkeyCar
import cv2
from donkeycar.parts.interpreter import KerasInterpreter  # For TensorFlow model interpretation
from donkeycar.parts.keras import KerasLinear  # For Keras-based linear models
import Adafruit_PCA9685  # Library for PWM control
import RPi.GPIO as GPIO  # Library for GPIO pin control on Raspberry Pi
import smbus2  # Library for I2C communication
import numpy as np

"""
Initialize color detection parameters
"""
# Define HSV color ranges for detecting red and green colors
lower_red = np.array([165, 150, 100])  # Lower bound for red
upper_red = np.array([179, 255, 255])  # Upper bound for red
lower_green = np.array([35, 50, 50])  # Lower bound for green
upper_green = np.array([85, 255, 255])  # Upper bound for green

red_detected = False  # Flag for detecting red color

'''
Initialize gyroscope sensor
'''
DEVICE_ADDRESS = 0x50  # I2C address of the gyroscope sensor
GYRO_Z_REGISTER = 0x39  # Register for Z-axis gyroscope data
bus = smbus2.SMBus(1)  # Initialize the I2C bus
yaw_angle = 0  # Variable to track yaw angle
previous_time = time.time()  # Track time for gyro calculations

parking_flag = True  # Flag indicating parking mode

'''
Setup PWM default values
'''
default_servo_signal = 350  # Default throttle signal
default_servo_steering_signal = 310  # Default steering signal
speed_limit = 326  # Speed limit for throttle

'''
Initialize GPIO pins
'''
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
gpio_Num = 25  # GPIO pin for the switch
GPIO.setup(gpio_Num, GPIO.IN, GPIO.PUD_UP)  # Set the GPIO pin as an input with pull-up

"""
Initialize PCA9685 PWM controller
"""
pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)  # Initialize PWM driver with I2C
pwm.set_pwm_freq(60)  # Set frequency for servos

# Helper function for setting servo pulse widths
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000  # 1,000,000 µs per second
    pulse_length //= 60  # 60 Hz
    pulse_length //= 4096  # 12-bit resolution
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Function to read Z-axis gyro data
def read_gyro_z():
    data = bus.read_i2c_block_data(DEVICE_ADDRESS, GYRO_Z_REGISTER, 2)  # Read 2 bytes from gyro
    gyro_z_raw = data[1] << 8 | data[0]  # Combine bytes into a 16-bit value
    if gyro_z_raw > 32767:  # Convert to signed value
        gyro_z_raw -= 65536
    gyro_z = gyro_z_raw / 32768.0 * 2000  # Scale to degrees per second
    return gyro_z

'''
Function for color detection
'''
def color_predict(frame):
    image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert frame to BGR
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # Convert to HSV
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)  # Mask for red color
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)  # Mask for green color
    red_count = cv2.countNonZero(mask_red)  # Count red pixels
    green_count = cv2.countNonZero(mask_green)  # Count green pixels
    return red_count

"""
Initialize camera
"""
IMAGE_W = 160  # Image width
IMAGE_H = 120  # Image height
IMAGE_DEPTH = 3  # Image depth
cam = PiCamera(image_w=IMAGE_W, image_h=IMAGE_H, image_d=IMAGE_DEPTH,
               vflip=False, hflip=False)

"""
Initialize TensorFlow model
"""
model_path = "/home/pi/airc_drive/model_obstaclerunccw01/mypilot.h5"  # Path to the trained model
input_shape = (120, 160, 3)  # Input shape for the model
interpreter = KerasInterpreter()  # TensorFlow interpreter
kl = KerasLinear(interpreter=interpreter, input_shape=input_shape)  # Initialize Keras model
kl.load(model_path)  # Load the model

'''
Main control loop
'''
# Initial setup for steering and throttle
for n in range(3):
    for i in range(5):  # Move straight
        pwm.set_pwm(1, 0, default_servo_steering_signal)
        pwm.set_pwm(0, 0, default_servo_signal)
        time.sleep(0.1)

    for i in range(5):  # Turn right
        pwm.set_pwm(1, 0, default_servo_steering_signal + 100)
        pwm.set_pwm(0, 0, default_servo_signal)
        time.sleep(0.1)

    for i in range(5):  # Turn left
        pwm.set_pwm(1, 0, default_servo_steering_signal - 100)
        pwm.set_pwm(0, 0, default_servo_signal)
        time.sleep(0.1)

# Wait for the switch to be turned on
while not GPIO.input(gpio_Num):
    pwm.set_pwm(1, 0, default_servo_steering_signal)
    pwm.set_pwm(0, 0, default_servo_signal)
    print("Turn off switch")
    time.sleep(0.1)

while GPIO.input(gpio_Num):
    pwm.set_pwm(1, 0, default_servo_steering_signal)
    pwm.set_pwm(0, 0, default_servo_signal)
    print("Waiting for switch to be turned on")
    time.sleep(0.1)

# Main loop for autonomous control
main_run_flag = True
previous_time = time.time()

while main_run_flag:
    # Read gyroscope data
    gyro_z = read_gyro_z()
    if gyro_z > 0:
        gyro_z *= 1.009

    current_time = time.time()
    delta_t = current_time - previous_time
    yaw_angle += gyro_z * delta_t
    previous_time = current_time

    # Stop if yaw angle exceeds limit or switch is off
    if GPIO.input(gpio_Num) or abs(yaw_angle) > 720:
        main_run_flag = False

    frame = PiCamera.run(cam)  # Capture camera frame

    # Detect red color when yaw angle is within range
    if 600 < abs(yaw_angle) < 660 and color_predict(frame) > 10:
        red_detected = True

    # Run model prediction
    outputs = KerasLinear.run(kl, img_arr=frame)
    print(f"Steering: {round(outputs[0], 2)}, Throttle: {round(outputs[1], 2)}")

    # Calculate PWM signals for steering and throttle
    servo_signal = int(round(outputs[1], 2) * -150 + default_servo_signal)
    servo_signal = max(min(servo_signal, 373), 327)
    servo_steering_signal = int(round(outputs[0], 2) * -135 + default_servo_steering_signal)
    servo_steering_signal = max(min(servo_steering_signal, default_servo_steering_signal + 150),
                                default_servo_steering_signal - 150)

    pwm.set_pwm(1, 0, servo_steering_signal)
    pwm.set_pwm(0, 0, servo_signal)

    time.sleep(0.01)

# Print final results
if red_detected:
    print("Red detected")
else:
    print("No red detected")

# Parking mode if enabled
if parking_flag:
    # Logic for parking mode
    pass

# Shutdown camera and cleanup
PiCamera.shutdown(cam)
cv2.destroyAllWindows()
