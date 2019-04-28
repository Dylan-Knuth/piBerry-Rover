
import RPi.GPIO as GPIO
import time

frontEcho=19
leftEcho=12
rightEcho=29

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

def reverse(sec):

 init()
 GPIO.output(17, False)
 GPIO.output(22, True)
 GPIO.output(23, False)
 GPIO.output(24, True)
 time.sleep(sec)


def stop(sec):
 init()
 GPIO.output(17, False)
 GPIO.output(22, False)
 GPIO.output(23, False)
 GPIO.output(24, False)
# GPIO.cleanup()
 time.sleep(sec)

def rightTurn(sec):
 init()
 GPIO.output(17, False)
 GPIO.output(22, False)
 GPIO.output(23, True)
 GPIO.output(24, False)
 time.sleep(sec)
 print "Turning Left...."

def leftTurn(sec):
 init()
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
	return distance


print "-------STARTING PiBerry-------"
frontDistance = frontSensor()
KeepGoing = True

try:		
	while KeepGoing:
		frontDistance=frontSensor()
		forward()

		if (frontDistance<=40.5):
			stop(1)
			if (frontDistance<25):
				stop(1.25)
				reverse(1)
				print "---Reversing\n*Beep* *Beep* *Beep*"
				frontDistance=frontSensor()
#				time.sleep(2)

			stop(2)
			print"---Checking Right Sensor"
			rightDistance=rightSensor()

			if(rightDistance>30):
				print"--Turning Right"
				rightTurn(0.5)
				stop(1.25)
				frontDistance=(frontSensor)
			
			elif(rightDistance<30):
				print "Checking Left Sensor"
				leftDistance=leftSensor()

				if(leftDistance>20):
					print "---Turing Left"
					leftTurn(0.5)
					stop(1.25)
					frontDistance=frontSensor()
					#rightDistance=rightSensor()
				else:
					print("STOPPING")
					KeepGoing=False
except KeyboardInterrupt:
	print('Kepboard--STOP')
finally:
 GPIO.cleanup()
