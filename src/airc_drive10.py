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

# ======================================================


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
model_path= current_path +"/model_frcw1/mypilot.h5"
input_shape = (120, 160, 3)
model_type = 'linear'
interpreter = KerasInterpreter()
kl = KerasLinear(interpreter=interpreter, input_shape=input_shape)
kl.load(model_path)




'''
run Main CODE
'''
# setup PMW "stop" and "central" data
default_servo_signal = 390
default_servo_steering_signal = 370
# setup car status
time_last = time.time()
# car_status forward:"1" ; backward:"-1" ; stop:"0"
car_status_now = int(0)
car_status_predict = int(0)



while True:

    frame = PiCamera.run(cam)
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    outputs = KerasLinear.run(kl,img_arr = frame)
    print("steering=",round(outputs[0],2),"throttle=",round(outputs[1],2))


#Prepare the PMW data
            

    servo_signal = int((round(outputs[1],2))*200+ default_servo_signal)
    if servo_signal > 400:
        servo_signal = int(400)
    if servo_signal < 300:
        servo_signal = int(300)
        

    servo_steering_signal = int((round(outputs[0],2))*100+ default_servo_steering_signal)
    if servo_steering_signal > 436:
        servo_steering_signal = int(436)
    if servo_steering_signal < 200:
        servo_steering_signal = int(200)


      

#output to 9685    

    pwm.set_pwm(1, 0, servo_steering_signal)
    pwm.set_pwm(0, 0, servo_signal)
    car_status_now = car_status_predict# renewal car status
    print("streeing PWM = ",servo_steering_signal)
    print("throttle PWM = ",servo_signal)
    car_status_now = car_status_predict

    time.sleep(0.1)


    #cv2.imshow('Camera Feed', frame)
     # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

PiCamera.shutdown(cam)
cv2.destroyAllWindows()
