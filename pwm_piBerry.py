
from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("car_start.mp3")

import RPi.GPIO as GPIO
import time

frontEcho=19
leftEcho=12
rightEcho=29

front_right=0
back_right=0
front_left=0
back_left=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) #front-right
GPIO.setup(22, GPIO.OUT) #back-right
GPIO.setup(23, GPIO.OUT) #front-left
GPIO.setup(24, GPIO.OUT) #back-left

front_right=GPIO.PWM(17, 110)
back_right=GPIO.PWM(22, 110)
front_left=GPIO.PWM(23, 110)
back_left=GPIO.PWM(24, 110)

front_right.start(0)
front_left.start(0)

back_right.start(0)
back_left.start(0)


def init():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(17, GPIO.OUT) #front-right
 GPIO.setup(22, GPIO.OUT) #back-right
 GPIO.setup(23, GPIO.OUT) #front-left
 GPIO.setup(24, GPIO.OUT) #back-left

def forward():
 front_right.ChangeDutyCycle(52.120000001)
 front_left.ChangeDutyCycle(54.251)


def reverse(sec):
 back_right.ChangeDutyCycle(95)
 back_left.ChangeDutyCycle(92)
 time.sleep(sec)


def stop(sec): 
 front_right.ChangeDutyCycle(0)
 front_left.ChangeDutyCycle(0) 
 back_right.ChangeDutyCycle(0)
 back_left.ChangeDutyCycle(0)
 time.sleep(sec)

def rightTurn(sec):
 #pin 23
# front_left=GPIO.PWM(17, 110)

 front_left.ChangeDutyCycle(100)
# back_right.ChangeDutyCycle(15)
 time.sleep(sec)
 print "Turning Right...."

def leftTurn(sec):
 front_right.ChangeDutyCycle(100)
# GPIO.output(17, True) 
 time.sleep(sec) 
 print "Turning Left...."

def frontSensor():
	GPIO.setmode(GPIO.BCM)
	PIN_TRIGGER = 26
	PIN_ECHO = 6
	GPIO.setup(PIN_TRIGGER, GPIO.OUT)
	GPIO.setup(PIN_ECHO, GPIO.IN)

	GPIO.output(PIN_TRIGGER, GPIO.LOW)

	time.sleep(0.05)

	GPIO.output(PIN_TRIGGER, GPIO.HIGH)

	time.sleep(0.00001)

	GPIO.output(PIN_TRIGGER, GPIO.LOW)

	while GPIO.input(PIN_ECHO)==0:
		pulse_start_time = time.time()
	while GPIO.input(PIN_ECHO)==1:
		pulse_end_time = time.time()

	pulse_duration = pulse_end_time - pulse_start_time
	distance = round(pulse_duration * 17150, 2)
	print "Front Distance:",distance,"cm"
#	GPIO.cleanup()
#	init()
	return distance

def rightSensor():
	GPIO.setmode(GPIO.BCM)
	PIN_TRIGGER = 19
	PIN_ECHO = 5
	GPIO.setup(PIN_TRIGGER, GPIO.OUT)
	GPIO.setup(PIN_ECHO, GPIO.IN)

	GPIO.output(PIN_TRIGGER, GPIO.LOW)

	time.sleep(0.05)

	GPIO.output(PIN_TRIGGER, GPIO.HIGH)

	time.sleep(0.00001)

	GPIO.output(PIN_TRIGGER, GPIO.LOW)

	while GPIO.input(PIN_ECHO)==0:
		pulse_start_time = time.time()
	while GPIO.input(PIN_ECHO)==1:
		pulse_end_time = time.time()

	pulse_duration = pulse_end_time - pulse_start_time
	distance = round(pulse_duration * 17150, 2)
	print "Right Distance:",distance,"cm"
#	GPIO.cleanup()
#	init()
	return distance

def leftSensor():
	GPIO.setmode(GPIO.BCM)
	PIN_TRIGGER = 13
	PIN_ECHO = 18
	GPIO.setup(PIN_TRIGGER, GPIO.OUT)
	GPIO.setup(PIN_ECHO, GPIO.IN)

	GPIO.output(PIN_TRIGGER, GPIO.LOW)

	time.sleep(0.05)

	GPIO.output(PIN_TRIGGER, GPIO.HIGH)

	time.sleep(0.00001)

	GPIO.output(PIN_TRIGGER, GPIO.LOW)

	while GPIO.input(PIN_ECHO)==0:
		pulse_start_time = time.time()
	while GPIO.input(PIN_ECHO)==1:
		pulse_end_time = time.time()

	pulse_duration = pulse_end_time - pulse_start_time
	distance = round(pulse_duration * 17150, 2)
	print "Left Distance:",distance,"cm"

#	GPIO.cleanup()
#	init()
	return distance


print "-------STARTING PiBerry(PWM)-------"
#init()
#frontDistance = frontSensor()

#play(song)

KeepGoing = True

try:
	while KeepGoing:
		frontDistance=frontSensor()

		forward()

		if (frontDistance<=12.5):
			stop(1)
			if (frontDistance<10):
				stop(1)
				print('REVERSING *BEEP* *BEEP*')
				reverse(0.35)
				stop(1)
				frontDistance=frontSensor()
			print('CHECKING RIGHT')
			rightDistance=rightSensor()
			
			if(rightDistance>25):
				stop(1)
				print('Turning Right')
				rightTurn(0.525)
				stop(0.25)
				frontDistance=frontSensor()
			elif(rightDistance<=24.9):
				stop(1)
				print('Checking Left')
				leftDistance=leftSensor()
				
				if(leftDistance>25):
					print('Turning Left')
					leftTurn(0.525)
					stop(1)
					frontDistance=frontSensor()
			else:
				print("STOPPING")
				KeepGoing=False

except KeyboardInterrupt:
	print('Kepboard--STOP')
	GPIO.cleanup()
