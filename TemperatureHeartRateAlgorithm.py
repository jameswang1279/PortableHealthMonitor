import serial

dataHeart = []
dataTemp = []
tempArray = []
counter = 0

while counter < 10:
	arduinoData = serial.Serial('COM5', 115200)
	#arduinoData = arduinoData.split(',')
	tempArray.append(arduinoData)
	counter += 1

print (tempArray)

'''
for i in range(len(tempArray)):
	tempArray[i] = float(tempArray[i])
for j in range(0,len(tempArray),2):
	dataTemp.append(tempArray[j])
for k in range(1,len(tempArray),2):
	dataHeart.append(tempArray[k])
'''
print (arduinoData)
print (dataTemp)
print (dataHeart)

 
