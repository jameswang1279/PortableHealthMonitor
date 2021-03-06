username = ' ';
password = ' ';
server = 'smtp.gmail.com:587';

import time
import datetime
from time import sleep;
import smtplib;
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText;
from email.mime.multipart import MIMEMultipart;
import serial


ctime = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
ser = serial.Serial('/dev/ttyUSB0', 9600)
a = ser.readline()
b = float(a)

def create_msg(to_address,
               from_address='',
               cc_address='',
               bcc_address='',
               subject=''):
    
    msg = MIMEMultipart();
    msg['Subject'] = subject;
    msg['To'] = to_address;
    msg['Cc'] = cc_address;
    msg['From'] = from_address;
    return msg;

def send_email(smtp_address, usr, password, msg, mode):
    server = smtplib.SMTP(smtp_address);
    server.ehlo();
    server.starttls();
    server.ehlo();
    server.login(username,password);
    if (mode == 0 and msg['To'] != ''):
        server.sendmail(msg['From'],(msg['To']+msg['Cc']).split(","), msg.as_string());
    elif (mode == 1 and msg['Bcc'] != ''):
        server.sendmail(msg['From'],msg['Bcc'].split(","),msg.as_string());
    elif (mode != 0 and mode != 1):
        print 'error in send mail bcc'; print 'email cancled'; exit();
    server.quit();


def compose_email(addresses, subject, body, files):

    # addresses
    to_address = addresses[0];
    cc_address = addresses[1];
    bcc_address = addresses[2];

    # create a message
    msg = create_msg(to_address, cc_address=cc_address , subject=subject);

    # add text
    for text in body:
        attach_text(msg, text[0], text[1]);

    # add files
    if (files != ''):
        file_list = files.split(',');
        for afile in file_list:
            attach_file(msg, afile);

    # send message
    send_email(server, username, password, msg, 0);

    # check for bcc
    if (bcc_address != ''):
        msg['Bcc'] = bcc_address;
        send_email(server, username, password, msg, 1);
        
    print 'email sent'

# attach text
# attaches a plain text or html text to a message

def attach_text(msg, atext, mode):
    part = MIMEText(atext, get_mode(mode));
    msg.attach(part);

# util function to get mode type

def get_mode(mode):
    if (mode == 0):
        mode = 'plain';
    elif (mode == 1):
        mode = 'html';
    else:
        print 'error in text kind'; print 'email cancled'; exit();
    return mode;

# attach file
# takes the message and a file name and attaches the file to the message

def attach_file(msg, afile):
    part = MIMEApplication(open(afile, "rb").read());
    part.add_header('Content-Disposition', 'attachment', filename=afile);
    msg.attach(part);


#///////////////////////////////////////////////////////

def tempMsg(a, condition, time):
    msg = ("As of %s your body temperature was %s Celsius, which is %s" %(ctime,b, condition))
    str(msg)
    global msg
    return msg
    

if(b > 35 and b < 39):
    print b
    condition = "normal"
    print condition
    tempMsg(b,condition,time)
  
elif(b > 39 and b < 40):
    print b
    condition = "low fever"
    print condition
    tempMsg(b,condition,time)
  
elif(b > 40):
    print b
    condition = "high fever"
    print condition
    tempMsg(b,condition,time)


compose_email([' ','',''],
              'Healthcare Monitoring System Data Report',
              [[msg,0]],
              'signal.png');
              
#compose_email can take the following arguments: 
#	1. to recipients (separated by a comma)
#	2. cc recipients (separated by a comma)
#	3. bcc recipients (separated by a comma)
#	4. subject
#	5. a list with message and mode (plain txt or html)
#	6. files to be attached
