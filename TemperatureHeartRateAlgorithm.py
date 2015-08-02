import serial
import numpy as np

A = [1,2,3,4]
B = [2,3,4,5]
C = [3,4,5,6]
D = [4,5,6,7]
dataBank = [A,B,C,D]

dataHeart = []
dataTemp = []
tempArray = []
counter = 0
averageT = 0
averageP = 0

while counter < 2: #debug counter
	arduinoData = '42,64'
	arduinoData = arduinoData.split(',')
	dataTemp.append(arduinoData[0])
	dataHeart.append(arduinoData[1])
	arduinoData = []
	counter += 1
	
for i in range(0,len(dataHeart)):
	dataHeart[i] = float(dataHeart[i])
for i in range(0,len(dataTemp)):
	dataTemp[i] = float(dataTemp[i])

averageT = np.mean(dataTemp)
averageP = np.mean(dataHeart)

if averageT < 38 and averageT > 36:
	conditionT = 'normal'
elif averageT > 38 and averageT < 39:
	conditionT = 'low fever'
elif averageT > 39:
	conditionT = 'high fever'
	
if averageP > 55 and averageP < 90:
	conditionP = 'normal'
elif averageP > 90 and averageP < 140:
	conditionP = 'high pulse if not exercising'
elif averageP > 140:
	conditionP = 'very high pulse'
elif averageP < 55:
	conditionP = 'low pulse' 

#Cross Validation between Heart Rate and Temperature Needed

print 'Average Temperature:',averageT
print 'Average Pulse:',averageP
print 'Temperature Condition:',conditionT 
print 'Pulse Condition:',conditionP

print dataBank[1][1] #Get error message from above conditionals from dataBank array
