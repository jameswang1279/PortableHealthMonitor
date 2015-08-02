import serial
import numpy as np

#formatted as of pulse,temperature
A = ['pulse parameter normal', 'temperature parameter normal'] #normal
B = ['Normal if exercising, otherwise diet should be maintained','Low fever detected'] #mild high
C = ['Get rest','High fever detected'] #very high
D = ['Pulse is low, exercise more','null'] #low

dataBank = [A,B,C,D]

dataHeart = []
dataTemp = []
tempArray = []
counter = 0
averageT = 0
averageP = 0

conditionPA = 0
conditionTA = 1

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
	conditionTR = 0 #used for reference dataBank
elif averageT > 38 and averageT < 39:
	conditionT = 'low fever'
	conditionTR = 1
elif averageT > 39:
	conditionT = 'high fever'
	conditionTR = 2
if averageP > 55 and averageP < 90:
	conditionP = 'normal'
	conditionPR = 0
elif averageP > 90 and averageP < 140:
	conditionP = 'high pulse if not exercising'
	conditionPR = 1
elif averageP > 140:
	conditionP = 'very high pulse'
	conditionPR = 2
elif averageP < 55:
	conditionP = 'low pulse'
	conditionPR =  3

#Cross Validation between Heart Rate and Temperature Needed

print 'Average Temperature:',averageT #debug  
print 'Average Pulse:',averageP
print 'Temperature Condition:',conditionT 
print 'Pulse Condition:',conditionP
print 'Temperature Message: ',dataBank[conditionTR][conditionTA]
print 'Pulse Message: ',dataBank[conditionPR][conditionPA]


