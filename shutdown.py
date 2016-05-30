#!/usr/bin/env python
import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)
PIN_INPUT = 22
PIN_INPUT2 = 23
GPIO.setup(PIN_INPUT, GPIO.OUT)
GPIO.setup(PIN_INPUT2, GPIO.IN)
GPIO.output(PIN_INPUT,True)

while(True):
	READ = GPIO.input(PIN_INPUT2)
	READ1 = GPIO.input(PIN_INPUT)
	print "Pin 23: "
	print READ
	print "!!!Pin 22: "
	print READ1
	if READ == False:
		#ATTIVA LA PROCEDURA DI SPEGNIMENTO
		shutdown_time = 5 #Max 30
		time.sleep(shutdown_time)
		GPIO.output(PIN_INPUT,False)
		os.system("shutdown -h now")
