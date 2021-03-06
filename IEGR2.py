import math
import matplotlib.pyplot as plt
import numpy as np
import serial
from pylab import *
import time
import datetime
import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'CenterAED001KKABA@gmail.com'
password = 'administrator%^&'
server = 'smtp.gmail.com:587'

ctime = datetime.datetime.strftime(datetime.datetime.now(),
                                   '%Y-%m-%d %H:%M:%S')

arduinoData = serial.Serial('/dev/ttyUSB0', 9600)
counter = 0
temperature = []
plt.ion


def makeFig():
    plt.xlim(0, 300)
    plt.ylim(35, 40)
    plt.title('Body Temperature Log')
    plt.grid(True)
    plt.ylabel('Temperature (Celsius) ')
    plt.plot(temperature, 'ro-', label='Degrees Celsius')
    plt.legend(loc='upper left')
    savefig('signal.png', dpi=100)
    plt.show()
    plt.draw()


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


def tempMsg(a, condition, time):
    msg = 'As of %s your body temperature was %s Celsius, which is %s'\
        % (ctime, averageT, condition)
    str(msg)
    global msg
    return msg

while True:
	counter += 1
	currentlog = 0.0891*(math.log(counter))+36.621
	
	data = float(arduinoData.readline().rstrip('\r\n'))
	if counter > 300:
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
					makeFig()
					#break
				elif averageT > 38 and averageT < 39:
					condition = 'low fever'
					print condition
					makeFig()
					#break
				elif averageT > 39:
					condition = 'high fever'
					print condition
					makeFig()
					#break
				tempMsg(averageT, condition, time)
				compose_email(['jameswang1279@gmail.com', '', ''], 'Healthcare Monitoring System Data Report',[[msg, 0]], 'signal.png')
		
				break
		else:
			print 'Data Invalid'
			print currentlog
			print data
			print ' '
	       
	





