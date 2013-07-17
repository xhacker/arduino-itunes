#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
from itunes import iTunes

print "Arduino iTunes Remote Controller"

ser = serial.serial_for_url("/dev/tty.ArduinoBluetooth", 9600, timeout=1)

while True:
	data = ser.readline().strip()
	if data:
		print data
	
	p = iTunes()
	if data == "PLAY":
		p.playpause()
	elif data == "PREV":
		p.previous()
	elif data == "NEXT":
		p.next()
	else:
		try:
			volume = int(data)
		except ValueError:
			pass
		else:
			p.volume = volume
