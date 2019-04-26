
import RPi.GPIO as GPIO
import time
import msvcrt


def init():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(17, GPIO.OUT)
 GPIO.setup(22, GPIO.OUT)
 GPIO.setup(23, GPIO.OUT)
 GPIO.setup(24, GPIO.OUT)


def forward():
 init()
 GPIO.output(17, True)
 GPIO.output(22, False)
 GPIO.output(23, True)
 GPIO.output(24, False)


def reverse():

 init()
 GPIO.output(17, False)
 GPIO.output(22, True)
 GPIO.output(23, False)
 GPIO.output(24, True)


def stop():
 init()
 GPIO.output(17, False)
 GPIO.output(22, False)
 GPIO.output(23, False)
 GPIO.output(24, False)
 GPIO.cleanup()


def rightTurn():
 init()
 GPIO.output(17, False)
 GPIO.output(22, False)
 GPIO.output(23, True)
 GPIO.output(24, False)


def leftTurn():
 init()
 GPIO.output(17, True)
 GPIO.output(22, False)
 GPIO.output(23, False)
 GPIO.output(24, False)
 



print ("-------STARTING PiBerry-------")
try:	
	command = msvcrt.getche()

	while command != 'q':
		while command == "w":
		 	print('Forward')

		while command == "s":
		 	print('Reverse')


		while command == "a":
		 	print('Left')

		while command == "d":
		 	print('Right')

finally:
 GPIO.cleanup()
