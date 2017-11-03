import serial
import time
ser = serial.Serial("COM5", 9600)
time.sleep(5)
print("sent")
ser.write(90)
