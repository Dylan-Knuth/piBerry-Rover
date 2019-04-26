
import RPi.GPIO as GPIO
import time

frontEcho=19
leftEcho=12
rightEcho=29

front_right=0
back_right=0
front_left=0
back_left=0

def init():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(17, GPIO.OUT) #front-right
 GPIO.setup(22, GPIO.OUT) #back-right
 GPIO.setup(23, GPIO.OUT) #front-left
 GPIO.setup(24, GPIO.OUT) #back-left

 front_right=GPIO.PWM(17, 100)
 back_right=GPIO.PWM(22, 100)
 front_left=GPIO.PWM(23, 100)
 back_left=GPIO.PWM(24, 100)


def forward():
 front_right.ChangeDutyCycle(50)
 front_left.ChangeDutyCycle(50)
 init()


def reverse(sec):

 #init()
 GPIO.output(17, False)
 GPIO.output(22, True)
 GPIO.output(23, False)
 GPIO.output(24, True)
 time.sleep(sec)


def stop(sec):
 #init()
 GPIO.output(17, False)
 GPIO.output(22, False)
 GPIO.output(23, False)
 GPIO.output(24, False)
# GPIO.cleanup()
 time.sleep(sec)

def rightTurn(sec):
 #init()
 GPIO.output(17, False)
 GPIO.output(22, False)
 GPIO.output(23, True)
 GPIO.output(24, False)
 time.sleep(sec)
 print "Turning Left...."

def leftTurn(sec):
 #init()
 GPIO.output(17, True)
 GPIO.output(22, False)
 GPIO.output(23, False)
 GPIO.output(24, False)
 time.sleep(sec) 
 print "Turning Right...."

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
	GPIO.cleanup()
	init()
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
	GPIO.cleanup()
	init()
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
	GPIO.cleanup()
	init()
	return distance


print "-------STARTING PiBerry(PWM)-------"

#frontDistance = frontSensor()
KeepGoing = True
init()

try:		
	while KeepGoing:
#		frontDistance=frontSensor()
		forward()

		# if (frontDistance<=40.5):
		# 	stop(1)

		# 	print("STOPPING")
		# 	KeepGoing=False
except KeyboardInterrupt:
	print('Kepboard--STOP')
finally:
 GPIO.cleanup()
