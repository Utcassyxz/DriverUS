'''
Extremely simple code that detects whether the on/off switch is connected to raspberry pi
'''

# Imports the GPIO library
import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbering

# GPIO connection slot on the raspberry pi 
gpio_Num = 25 
GPIO.setup(gpio_Num, GPIO.IN,GPIO.PUD_UP)

# Prints the GPIO connection signal
while True:
    print(GPIO.input(gpio_Num))
    time.sleep(0.1)

