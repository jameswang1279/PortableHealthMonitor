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

ctime = datetime.datetime.strftime(datetime.datetime.now(),
                                   '%Y-%m-%d %H:%M:%S')

'''End Analysis Information'''

#<!-------------------------------------------->
'''Plot Information'''

def makeFig():
    plt.xlim(0, 300)
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
    msg = 'As of %s your average pulse rate was %d, which is %s. Messages regarding your pulse: %s. Your body temperature was %s Celsius, which is %s. Message regarding your body temperature: %s. '\
        % (ctime, averageP, conditionP, msgP, averageT, conditionT, msgT )
    str(msg)
    global msg
    return msg


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

print 'Average Temperature:',averageT   
print 'Average Pulse:',averageP
print 'Temperature Condition:',conditionT 
print 'Pulse Condition:',conditionP
print 'Temperature Message: ',dataBank[conditionTR][conditionTA]
print 'Pulse Message: ',dataBank[conditionPR][conditionPA]
makeFig()

msgT = dataBank[conditionTR][conditionTA]
msgP = dataBank[conditionPR][conditionPA]

tempMsg(ctime, averageP, conditionP, msgP, averageT, conditionT, msgT)
compose_email(['jameswang1279@gmail.com', '', ''], 'Healthcare Monitoring System Data Report',[[msg, 0]], 'signal.png')

