#!/usr/bin/env python
import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)
PIN_INPUT = 22 #!pin che indica al PiSaver lo stato Accesso/Spento della Raspberry - Acceso=1; Spento=0;
PIN_INPUT2 = 23 #!pin che indica alla raspberry di eseguire la funzione di spegnimento - 0=Spegni
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
		print "Attivo Procedura di Spegnimento"
		shutdown_time = 2 #Max 30
		time.sleep(shutdown_time)
		GPIO.output(PIN_INPUT,False)
		time.sleep(shutdown_time)
		os.system("shutdown -h now")
