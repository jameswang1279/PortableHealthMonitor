import serial
import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import *
import time
import datetime
from time import sleep
import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

'''Analysis Information'''

#formatted as of pulse,temperature
A = ['pulse parameter normal', 'temperature parameter normal', 'air quality is normal and safe'] #normal
B = ['Normal if exercising, otherwise diet should be maintained','Low fever detected','pollutants detected','avoid prolonged exposure'] #mild high
C = ['Get rest','High fever detected', 'high amounts of pollutants detected, get out of area immediately'] #very high
D = ['Pulse is low, exercise more','null data, remeasure', 'air quality is normal and safe'] #low


dataBank = [A,B,C,D]

dataHeart = []
dataTemp = []
dataPoll = []
counter = 0
averageT = 0
averageP = 0
averagePO = 0
index = []

conditionPA = 0
conditionTA = 1
conditionPO = 2

sThreshPO = 1000 #SUDO
mThreshPO = 1500 #SUDO
dThreshPO = 2000 #SUDO
ddThreshPO = 2200 #SUDO

ctime = datetime.datetime.strftime(datetime.datetime.now(),
                                   '%Y-%m-%d %H:%M:%S')

ser = serial.Serial('/dev/ttyACM0', 115200)

'''End Analysis Information'''

#<!-------------------------------------------->
'''Plot Information'''

def makeFig():
    plt.xlim(0, len(dataTemp))
    plt.ylim(35, 40)
    plt.title('Body Temperature Log')
    plt.grid(True)
    plt.ylabel('Temperature (Celsius) ')
    plt.plot(dataTemp, 'ro-', label='Degrees Celsius')
    plt.legend(loc='upper left')
    savefig('signal.png', dpi=100)
    plt.show()
    plt.draw()


#<!-------------------------------------------->

'''Server Information'''

username = 'CenterAED001KKABA@gmail.com'
password = 'administrator%^&'
server = 'smtp.gmail.com:587'

def create_msg(
    to_address,
    from_address='',
    cc_address='',
    bcc_address='',
    subject='',
    ):

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['To'] = to_address
    msg['Cc'] = cc_address
    msg['From'] = from_address
    return msg


def send_email(
    smtp_address,
    usr,
    password,
    msg,
    mode,
    ):

    server = smtplib.SMTP(smtp_address)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    if mode == 0 and msg['To'] != '':
        server.sendmail(msg['From'], (msg['To'] + msg['Cc']).split(','
                        ), msg.as_string())
    elif mode == 1 and msg['Bcc'] != '':
        server.sendmail(msg['From'], msg['Bcc'].split(','),
                        msg.as_string())
    elif mode != 0 and mode != 1:
        print 'error in send mail bcc'
        print 'email cancled'
        exit()
    server.quit()


def compose_email(
    addresses,
    subject,
    body,
    files,
    ):

    # addresses

    to_address = addresses[0]
    cc_address = addresses[1]
    bcc_address = addresses[2]

    msg = create_msg(to_address, cc_address=cc_address, subject=subject)

    for text in body:
        attach_text(msg, text[0], text[1])

    if files != '':
        file_list = files.split(',')
        for afile in file_list:
            attach_file(msg, afile)

    send_email(server, username, password, msg, 0)

    if bcc_address != '':
        msg['Bcc'] = bcc_address
        send_email(server, username, password, msg, 1)

    print 'email sent'


def attach_text(msg, atext, mode):
    part = MIMEText(atext, get_mode(mode))
    msg.attach(part)


def get_mode(mode):
    if mode == 0:
        mode = 'plain'
    elif mode == 1:
        mode = 'html'
    else:
        print 'error in text kind'
        print 'email cancled'
        exit()
    return mode


def attach_file(msg, afile):
    part = MIMEApplication(open(afile, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=afile)
    msg.attach(part)

'''End Server Information'''
#<!----------------------------------------------------> Generate Message for Email

def tempMsg(ctime, averageP, conditionP, msgP, averageT, conditionT, msgT ): #NEED TO CHANGE VAR NAME
    msg = 'As of %s your average pulse rate was %d, which is %s. Remarks regarding your pulse: %s. Your body temperature was %s Celsius, which is %s. Remarks regarding your body temperature: %s. Pollution in the vicinity is at %d, which is %s.'\
        % (ctime, averageP, conditionP, msgP, averageT, conditionT, msgT, averagePO, conditionPO, conditionPO )
    str(msg)
    global msg
    return msg


while counter <= 20: #debug counter
	arduinoData = ser.readline()
	print 'Data', arduinoData #Debug purpose
	#arduinoData = '42,64' #Single data Simulation0
	#if counter == 0: #Continuous data Simulation
	#	arduinoData = '42,63,1000'
	#elif counter == 1:
	#	arduinoData = '38,61,2000'
	#elif counter == 2:
	#	arduinoData = '12,58,3000'
	arduinoData = arduinoData.split(',')
	dataTemp.append(arduinoData[0])
	dataHeart.append(arduinoData[1])
	dataPoll.append(arduinoData[2])
	arduinoData = []
	counter += 1

makeFig()

for i in range(0,len(dataHeart)):
	dataHeart[i] = float(dataHeart[i])
for i in range(0,len(dataTemp)):
	dataTemp[i] = float(dataTemp[i])
for i in range(0,0): #STAYS AT 0,0 FOR SIMULATION PURPOSE
	dataTemp.pop[i]
for i in range(1,len(dataTemp)): 
	if(dataTemp[i] < ((0.0891*(math.log(i))+36.621)+1.5) or dataTemp[i] < ((0.0891*(math.log(i))+36.621)-1.5)):
		index.append(i)
for i in range(0,len(dataPoll[i]):
	dataPoll[i] = float(dataPoll[i])

dataTemp = np.delete(dataTemp, index)
print dataTemp

averageT = np.mean(dataTemp)
averageP = np.mean(dataHeart)
averagePO = np.mean(dataPoll)

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

if averagePO > sThreshPO and averagePO < mThreshPO:  
	conditionPO = 'normal'
	conditionPOR = 0
elif averagePO > mThreshPO and averagePO < dThreshPO: #UNDEFINED VARIABLES
	conditionPO = 'pollutants detected'
	conditionPOR = 1
elif averagePO > dThreshPO and averagePO < ddThreshPO: #UNDEFINED VARIABLES
	conditionPO = 'dangerous amounts of pollutants detected'
	conditionPOR = 2

#Cross Validation between Heart Rate and Temperature Needed

print 'Average Temperature:',averageT   
print 'Average Pulse:',averageP
print 'Average Pollution Index: ', averagePO
print 'Temperature Condition:',conditionT 
print 'Pulse Condition:',conditionP
print 'Pollution Index Condition', conditionPO
print 'Temperature Remarks: ',dataBank[conditionTR][conditionTA]
print 'Pulse Remarks: ',dataBank[conditionPR][conditionPA]
print 'Pollution Monitoring Remarks: ', dataBank[conditionPOR][conditionPOA]  


msgT = dataBank[conditionTR][conditionTA]
msgP = dataBank[conditionPR][conditionPA]
msgPO = dataBank[conditionPOR][conditionPOA]

tempMsg(ctime, averageP, conditionP, msgP, averageT, conditionT, msgT, averagePO, conditionPO, msgPO)
compose_email(['jameswang1279@gmail.com', '', ''], 'Healthcare Monitoring System Data Report',[[msg, 0]], 'signal.png')

