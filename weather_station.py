import serial
import time
import csv

serial = serial.Serial('dev/ttyUSB0')
ser.flushInput()

while True:
    try:
        serial_data = ser.readline()
        decoded_data = (ser_bytes).decode("utf-8")
        print(decoded_data)
    except:
        print("Script interrompido")
        break
