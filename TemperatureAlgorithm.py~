import math
import serial

arduinoData = serial.Serial('/dev/ttyUSB0', 9600)
counter = 0

while True:
	counter += 1
	currentlog = 0.0891*(math.log(counter))+36.621
	
	data = float(arduinoData.readline().rstrip('\r\n'))
	if counter > 40:
		if((data < (currentlog + 1)) and (data > (currentlog - 1))):
			print 'Data Valid'
			print currentlog
			print data
			print ' '
		else:
			print 'Data Invalid'
			print currentlog
			print data
			print ' '
