#!/usr/bin/env python
import RPi.GPIO as GPIO
import os
import time
import serial
import urllib2

GPIO.setmode(GPIO.BCM)
PIN_INPUT = 22
PIN_INPUT2 = 23
#GPIO.setup(PIN_INPUT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_INPUT, GPIO.OUT)
GPIO.setup(PIN_INPUT2, GPIO.IN)
GPIO.output(PIN_INPUT,True)
ser = serial.Serial("/dev/ttyACM0", 115200)
time.sleep(1)
ser.write("l99:reset:-")


while(True):
	READ = GPIO.input(PIN_INPUT2)
	READ1 = GPIO.input(PIN_INPUT)
	print "Pin 23: "
	print READ
	print "!!!Pin 22: "
	print READ1
	if READ == False:
			#ATTIVA LA PROCEDURA DI SPEGNIMENTO
		urllib2.urlopen("http://localhost:8083/apio/shutdown").read()
		GPIO.output(PIN_INPUT,False)
		time.sleep(5)
