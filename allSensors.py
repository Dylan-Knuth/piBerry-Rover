#!/usr/bin/python
import RPi.GPIO as GPIO
import time

def frontSensor():
	GPIO.setmode(GPIO.BCM)
	PIN_TRIGGER = 26
	PIN_ECHO = 6
	GPIO.setup(PIN_TRIGGER, GPIO.OUT)
	GPIO.setup(PIN_ECHO, GPIO.IN)

	GPIO.output(PIN_TRIGGER, GPIO.LOW)

	time.sleep(2)

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

	time.sleep(2)

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

	time.sleep(2)

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

while True:
	print "Calculating Distances:\n"
	frontSensor()
	rightSensor()
	leftSensor()
	break