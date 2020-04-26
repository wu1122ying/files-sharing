#!/usr/bin/python
# -*- coding:utf-8 _*_

import serial
import time
ser = serial.Serial('/dev/ttyAMA0',57600)

#print('serial test staart ...')
if ser.isOpen == False:
    ser.open()
ser.write(b'it is ok ')

try:
     while True:
         size = ser.inWaiting()
         if size != 0:
             response = ser.read(size)
             print (response)
             time.sleep(0.1)
#             ser.write(ser.red())
#except KeyboardInterrupt:
#           if ser != None:
#               ser.close()
except KeyboardInterrupt:
    ser.close()