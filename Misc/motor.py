# GPIO 12 , 16 Motor Right
# GPIO 20 , 21 Motor Left
motorLeftP = 20
motorLeftN = 21
motorRightP = 12
motorRightN = 16

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(motorLeftP,GPIO.OUT)
GPIO.setup(motorLeftN,GPIO.OUT)
GPIO.setup(motorRightP,GPIO.OUT)
GPIO.setup(motorRightN,GPIO.OUT)

def forward():
    GPIO.output(motorLeftP,GPIO.HIGH)
    GPIO.output(motorLeftN,GPIO.LOW)
    GPIO.output(motorRightP,GPIO.HIGH)
    GPIO.output(motorRightN,GPIO.LOW)

def backward():
    GPIO.output(motorLeftP,GPIO.LOW)
    GPIO.output(motorLeftN,GPIO.HIGH)
    GPIO.output(motorRightP,GPIO.LOW)
    GPIO.output(motorRightN,GPIO.HIGH)

def left():
    GPIO.output(motorLeftP,GPIO.LOW)
    GPIO.output(motorLeftN,GPIO.LOW)
    GPIO.output(motorRightP,GPIO.HIGH)
    GPIO.output(motorRightN,GPIO.LOW)

def right():
    GPIO.output(motorLeftP,GPIO.HIGH)
    GPIO.output(motorLeftN,GPIO.LOW)
    GPIO.output(motorRightP,GPIO.LOW)
    GPIO.output(motorRightN,GPIO.LOW)

def stop():
    GPIO.output(motorLeftP,GPIO.LOW)
    GPIO.output(motorLeftN,GPIO.LOW)
    GPIO.output(motorRightP,GPIO.LOW)
    GPIO.output(motorRightN,GPIO.LOW)



while True:
    dir = input()
    if dir=='8':
        forward()
    elif dir=='2':
        backward()
    elif dir=='4':
        left()
    elif dir=='6':
        right()
    else:
        stop()
        break

stop()
print('stopped')