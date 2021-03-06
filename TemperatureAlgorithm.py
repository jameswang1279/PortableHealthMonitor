import math
import serial
import numpy as np

arduinoData = serial.Serial('/dev/ttyUSB0', 9600)
counter = 0
temperature = []

while True:
	counter += 1
	currentlog = 0.0891*(math.log(counter))+36.621
	
	data = float(arduinoData.readline().rstrip('\r\n'))
	if counter > 40:
		if((data < (currentlog + 1.5)) and (data > (currentlog - 1.5))):
			print 'Data Valid'
			print currentlog
			print data
			print ' '
			temperature.append(data)
			if(len(temperature) > 300):
				averageT = np.mean(temperature)
				print averageT
				if averageT < 38 and averageT > 36:
					condition = 'normal'
					print condition
					break
				elif averageT > 38 and averageT < 39:
					condition = 'low fever'
					print condition
					break
				elif averageT > 39:
					condition = 'high fever'
					print condition
					break
		else:
			print 'Data Invalid'
			print currentlog
			print data
			print ' '
