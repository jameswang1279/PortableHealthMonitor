import serial
import string

dataSeries = []

arduinoData = '5,3,4,5,6,7'
#arduinoData = serial.Serial('/dev/ttyUSB0', 115200)
dataSeries.append(arduinoData)
dataSeries = dataSeries.strip(',')


print dataSeries
