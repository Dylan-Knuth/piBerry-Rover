import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

sensor = Adafruit_DHT.DHT22
pin = 25
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#temperature = temperature * 9/5.0 + 32

if humidity is not None and temperature is not None:
	temperature = temperature * 9/5.0 + 32

	print('Temperature = {0:00.1f}* Humidity {1:0.1f}%'.format(temperature, humidty))
else:
	print('Failed to get reading. try again!')
	sys.exit(1)
