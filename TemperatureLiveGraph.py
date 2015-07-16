#Need to install pillow

import matplotlib.pyplot as plt
import numpy as np
import serial
from drawnow import *

temperature = []
arduinoData = serial.Serial('COM4', 115200)
plt.ion
cnt = 0

def makeFig():
    plt.xlim(0,100)
    plt.ylim(35,45)
    plt.title("Body Temperature Log")
    plt.grid(True)
    plt.ylabel("Temperature (Celsius) ")
    plt.plot(temperature, 'ro-',leabel = 'Degrees Celsius')
    plit.legend(loc = 'upper left')

while True:
            while(arduinoData.inWaiting() ==0):
                pass
            arduinoString = arduinoData.readline()
            temp = float(dataArray[0])
            temperature.append(temp)
            drawnoe(makeFig)
            plt.pause(0.0001)
            if(cent > 50):
                    temp.pop(0)
            if((numpy.max(temperature[:,0])) > 42):
                plt.savefig('image.jpg')
            
