import serial
import smtplib
import time
import string

fromaddr = ''
toaddrs = ''
username = ' '
password = ''
server = smtplib.SMTP('smtp.gmail.com:587')

condition = "null"

def tempMsg(a, condition, time):
    msg = ("As of %s your body temperature was %s Celsius, which is %s" %('null' a, condition))
    str(msg)
    return msg

    
time =time.ctime()
ser = serial.Serial('COM4')
a = ser.readline()
b = float(a)
if(b > 35 and b < 39):
    print b
    condition = "normal"
    print condition
    msg1 = tempMsg(b,condition,time)
  
elif(b > 39 and b < 40):
    print b
    condition = "low fever"
    print condition
    msg1 = tempMsg(b,condition,time)
  
elif(b > 40):
    print b
    condition = "high fever"
    print condition
    msg1 = tempMsg(b,condition,time)
    

    #msg = "Your temperature was recorded as of normal as of %s. Your temperature was %s Celsius" %("[null]", a)
    
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg1)
server.quit()

print "Message Sent as of %s!" %(time)

