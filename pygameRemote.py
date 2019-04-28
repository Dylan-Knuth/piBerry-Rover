import pygame
from pygame.locals import *
import RPi.GPIO as GPIO
import time

pygame.init()
pygame.display.set_mode((100, 100))


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
 #print "Turning Right...."


def leftTurn():
 init()
 GPIO.output(17, True)
 GPIO.output(22, False)
 GPIO.output(23, False)
 GPIO.output(24, False)




print ("-------STARTING Remote PiBerry-------")
pressed=pygame.key.get_pressed()

while True:
	for event in pygame.event.get():
	    if event.type==pygame.KEYDOWN:
	        if event.key == pygame.K_UP:
	           print('Forward')
		   forward()
		elif event.key == pygame.K_DOWN:
		   print('Reverse')
		   reverse()
		elif event.key == pygame.K_RIGHT:
                   print('Right')
		   rightTurn()
		elif event.key == pygame.K_LEFT:
                   print('Left')
		   leftTurn()
		elif event.key == pygame.K_SPACE:
                   print('STOP')
                   stop()
		elif event.key == pygame.K_q:
                   print('Goodbye')
		   stop()
		   pygame.quit()
		   break
