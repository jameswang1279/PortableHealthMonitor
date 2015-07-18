#Need to install pillow
	
import matplotlib.pyplot as plt
import numpy as np
import serial
from pylab import *
#from drawnow import *

temperature = []
arduinoData = serial.Serial('/dev/ttyUSB0', 9600)
plt.ion
cnt = 0

def makeFig():
    plt.xlim(0,100)
    plt.ylim(35,45)
    plt.title("Body Temperature Log")
    plt.grid(True)
    plt.ylabel("Temperature (Celsius) ")
    plt.plot(temperature, 'ro-',label = 'Degrees Celsius')
    plt.legend(loc = 'upper left')
    savefig("signal.png",dpi=100)
    plt.show()
    plt.draw()
while True:
            while(arduinoData.inWaiting() ==0):
                pass
            temp = arduinoData.readline()
            #temp = float(dataArray[0])
	    #temp = arduinoString
            temperature.append(temp)
            #drawnow(makeFig)
            plt.pause(0.0001)
            cnt += 1
            print (cnt)
            if(cnt > 33):
                    temperature.pop()
                    print ("FULL!!!!")
                    print ("Saving images...")
                    #plt.savefig('image.jpg')
                    makeFig()
                   # save("signal", ext="svg", close=True, verbose=True)
                   # savefig('foo.png', bbox_inches='tight')
                    break	
           # if((np.max(temperature)) > 42):
            #    plt.savefig('image.jpg')
            
