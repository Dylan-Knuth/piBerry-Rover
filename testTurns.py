
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) #front-right
GPIO.setup(22, GPIO.OUT) #back-right
GPIO.setup(23, GPIO.OUT) #front-left
GPIO.setup(24, GPIO.OUT) #back-left

front_right=GPIO.PWM(17, 100)
back_right=GPIO.PWM(22, 100)
front_left=GPIO.PWM(23, 100)
back_left=GPIO.PWM(24, 100)

front_right.start(0)
front_left.start(0)

back_right.start(0)
back_left.start(0)



def rightTurn(sec):
 #front_left.ChangeDutyCycle(90) 
 GPIO.output(23, True) 
 time.sleep(sec)
 print "Turning Right...."



def leftTurn(sec):
 #front_right.ChangeDutyCycle(100) 
 GPIO.setup(17, GPIO.OUT)
 GPIO.output(17, True)
 time.sleep(sec)
 print "Turning Left...."

#rightTurn(0.5)
leftTurn(0.5)
GPIO.cleanup()

