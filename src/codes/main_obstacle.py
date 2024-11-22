'''
This is a very basic program that uses donkeycar camera images to feed a keras model to make predictions.
'''

import os
import time
import sys
current_path = os.getcwd()
sys.path.append(current_path)
from donkeycar.parts.camera import PiCamera
import cv2
from donkeycar.parts.interpreter import KerasInterpreter
from donkeycar.parts.keras import KerasLinear
import Adafruit_PCA9685
import RPi.GPIO as GPIO
import smbus2
import numpy as np

"""
init color detect 
"""
# Define color ranges for red and green in HSV color space
lower_red = np.array([165, 150, 100])  # Lower range for red (Hue: 170-179, Saturation: 120-255, Value: 100-255)
upper_red = np.array([179, 255, 255])  # Upper range for red (Hue: 170-179, Saturation: 120-255, Value: 100-255)
# Green Range: Hue 30-80 (adjust based on your preference)
lower_green = np.array([35, 50, 50])  # Lower hue for green (from 30 to 40) and lower saturation/brightness
upper_green = np.array([85, 255, 255])  # Upper hue for green (from 40 to 80) and full saturation/brightness

red_detected = False

'''
init GYRO Sensor
'''
# I2C address of the WT901 sensor (default is 0x50)remedyauthor917
DEVICE_ADDRESS = 0x50
# Gyro Z register
GYRO_Z_REGISTER = 0x39  # Example register for Z-axis gyroscope

# Initialize the I2C bus
bus = smbus2.SMBus(1)

# Variable to store the yaw angle
yaw_angle = 0

# Time tracking for integration
previous_time = time.time()

parking_flag = True

# setup PMW "stop" and "central" data
default_servo_signal = 350
default_servo_steering_signal = 310
speed_limit = 326

'''
init GPIO
'''
# Set the GPIO mode
GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbering
gpio_Num = 25 
GPIO.setup(gpio_Num, GPIO.IN,GPIO.PUD_UP)

"""
init pwm9685
"""
# pwm = Adafruit_PCA9685.PCA9685()
# Alternatively specify a different address and/or bus:
pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)
# Configure min and max servo pulse lengths
# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)


def read_gyro_z():
    # Read two bytes from the gyro Z register
    data = bus.read_i2c_block_data(DEVICE_ADDRESS, GYRO_Z_REGISTER, 2)
    # Combine the two bytes into a 16-bit value
    gyro_z_raw = data[1] << 8 | data[0]
    
    # Convert the raw gyroscope value to angular velocity in degrees per second
    # (You might need to adjust the scale depending on your gyro's sensitivity)
    if gyro_z_raw > 32767:
        gyro_z_raw -= 65536
    gyro_z = gyro_z_raw / 32768.0 * 2000  # Assuming +/- 2000 dps range, adjust if needed
    return gyro_z
# ======================================================

#Color detection program via saturation mask
def color_predict(frame):
    image = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Create masks for red and green colors
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)

    # Count non-zero pixels in each mask to detect the presence of color
    red_count = cv2.countNonZero(mask_red)
    green_count = cv2.countNonZero(mask_green)
#     print('red_count=',red_count)
#     print('green_count=',green_count)
    
    return red_count









servo_steering_signal= 0
servo_signal= 0

"""
init camera
from dondeycar/parts/camera
"""
IMAGE_W = 160
IMAGE_H = 120
IMAGE_DEPTH = 3
cam = PiCamera(image_w=IMAGE_W, image_h=IMAGE_H, image_d=IMAGE_DEPTH,
                 vflip=False, hflip=False)


# """
# init tf and models
# """
model_path="/home/pi/airc_drive/model_obstaclerunccw01/mypilot.h5"
input_shape = (120, 160, 3)
model_type = 'linear'
interpreter = KerasInterpreter()
kl = KerasLinear(interpreter=interpreter, input_shape=input_shape)
kl.load(model_path)




'''
run Main CODE
'''

for n in range(0,3):
    for i in range(0,5):
        pwm.set_pwm(1, 0, default_servo_steering_signal)
        pwm.set_pwm(0, 0, default_servo_signal)
        time.sleep(0.1)   

    for i in range(0,5):
        pwm.set_pwm(1, 0, default_servo_steering_signal+100)
        pwm.set_pwm(0, 0, default_servo_signal)
        time.sleep(0.1)
        
    for i in range(0,5):
        pwm.set_pwm(1, 0, default_servo_steering_signal-100)
        pwm.set_pwm(0, 0, default_servo_signal)
        time.sleep(0.1)    
          
     

while (not GPIO.input(gpio_Num)):
    pwm.set_pwm(1, 0, default_servo_steering_signal)
    pwm.set_pwm(0, 0, default_servo_signal)
    print("turn off switch")
    time.sleep(0.1)
    
while (GPIO.input(gpio_Num)):
    pwm.set_pwm(1, 0, default_servo_steering_signal)
    pwm.set_pwm(0, 0, default_servo_signal)
    print("waiting for switch to be turned on")
    time.sleep(0.1)



main_run_flag = True
# Time tracking for integration
previous_time = time.time()
# setup car status
time_last = time.time()

while (main_run_flag):
    
    gyro_z = read_gyro_z()
    if gyro_z > 0:
        gyro_z = gyro_z * 1.009

    # Get the current time
    current_time = time.time()

    # Calculate time difference (delta t)
    delta_t = current_time - previous_time

    # Update the yaw angle using gyro data (angular velocity * time)
    yaw_angle += gyro_z * delta_t

    # Update previous time for the next iteration
    previous_time = current_time
    #print('yaw_angle=',round(yaw_angle,2))
    
    if (GPIO.input(gpio_Num) or abs(yaw_angle) > 720):
        main_run_flag = False
    
    
    frame = PiCamera.run(cam)
    if abs(yaw_angle) >600 and abs(yaw_angle)<660:
        print(color_predict(frame))
        if color_predict(frame) > 10:
            red_detected = True
    #frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    outputs = KerasLinear.run(kl,img_arr = frame)
    print("steering=",round(outputs[0],2),"throttle=",round(outputs[1],2))
#     print(int((round(outputs[0],2))*(-200)+ default_servo_steering_signal-70))

    
#Prepare the PMW data
            

    servo_signal = int((round(outputs[1],2))*(-150)+ default_servo_signal)
    if servo_signal > 373:
        servo_signal = int(373)
    if servo_signal < 327:
        servo_signal = 327
        

    servo_steering_signal = int((round(outputs[0],2))*(-135)+ default_servo_steering_signal)
    if servo_steering_signal > default_servo_steering_signal+150:
        servo_steering_signal = int(default_servo_steering_signal+150)
    if servo_steering_signal < default_servo_steering_signal-150:
        servo_steering_signal = int(default_servo_steering_signal-150)


      

#output to 9685    

    pwm.set_pwm(1, 0, servo_steering_signal)
    pwm.set_pwm(0, 0, servo_signal)

    print("streeing PWM = ",servo_steering_signal, "throttle PWM = ",servo_signal)



    time.sleep(0.01)


    #cv2.imshow('Camera Feed', frame)
     # Break the loop on 'q' key press

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
for i in range(0,10):
    pwm.set_pwm(1, 0, default_servo_steering_signal)
    pwm.set_pwm(0, 0, default_servo_signal)
    time.sleep(0.1)
    print('pwm out stop')

if red_detected :
    print('red detected')
else:
    print('No red ') 

for j in range(0,3):
    for i in range(0,6):
        pwm.set_pwm(1, 0, default_servo_steering_signal+150)
        pwm.set_pwm(0, 0, default_servo_signal-23)
        time.sleep(0.1)
    for i in range(0,6):
        pwm.set_pwm(1, 0, default_servo_steering_signal)
        pwm.set_pwm(0, 0, default_servo_signal)
        time.sleep(0.1)
    for i in range(0,6):
        pwm.set_pwm(1, 0, default_servo_steering_signal-150)
        pwm.set_pwm(0, 0, default_servo_signal+23)
        time.sleep(0.1)
    for i in range(0,6):
        pwm.set_pwm(1, 0, default_servo_steering_signal)
        pwm.set_pwm(0, 0, default_servo_signal)
        time.sleep(0.1)

if parking_flag :
    #=================================================================================
    #run parking
    model_path="/home/pi/airc_drive/model_obstaclerun_parking_ccw01/mypilot.h5"
    input_shape = (120, 160, 3)
    model_type = 'linear'
    interpreter = KerasInterpreter()
    kl = KerasLinear(interpreter=interpreter, input_shape=input_shape)
    kl.load(model_path)

    main_run_flag = True
    # Time tracking for integration
    previous_time = time.time()
    # setup car status
    time_last = time.time()

    while (main_run_flag):

        
        if GPIO.input(gpio_Num):
            main_run_flag = False
        
        
        frame = PiCamera.run(cam)
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        outputs = KerasLinear.run(kl,img_arr = frame)
        print("steering=",round(outputs[0],2),"throttle=",round(outputs[1],2))
    #     print(int((round(outputs[0],2))*(-200)+ default_servo_steering_signal-70))


    #Prepare the PMW data
                

        servo_signal = int((round(outputs[1],2))*(-150)+ default_servo_signal)
        if servo_signal > 373:
            servo_signal = int(373)
        if servo_signal < speed_limit:
            servo_signal = speed_limit
            

        servo_steering_signal = int((round(outputs[0],2))*(-150)+ default_servo_steering_signal)
        if servo_steering_signal > default_servo_steering_signal+200:
            servo_steering_signal = int(default_servo_steering_signal+200)
        if servo_steering_signal < default_servo_steering_signal-200:
            servo_steering_signal = int(default_servo_steering_signal-200)


          

    #output to 9685    

        pwm.set_pwm(1, 0, servo_steering_signal)
        pwm.set_pwm(0, 0, servo_signal)

        print("streeing PWM = ",servo_steering_signal, "throttle PWM = ",servo_signal)



        time.sleep(0.01)


        #cv2.imshow('Camera Feed', frame)
         # Break the loop on 'q' key press

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    for i in range(0,10):
        pwm.set_pwm(1, 0, default_servo_steering_signal)
        pwm.set_pwm(0, 0, default_servo_signal)
        time.sleep(0.1)
        print('pwm out stop')






PiCamera.shutdown(cam)
cv2.destroyAllWindows()


