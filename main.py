from weather_function import unpack_data # Função de unpack string -> dict
import serial
from time import sleep
import csv


serial = serial.Serial('dev/ttyUSB0')
serial.flushInput()

data_dict = {}

while True:
    try:
        for num in range(1, 3):
            serial_data = serial.readline()
            decoded_data = (serial_data).decode("utf-8")
            # print(decoded_data)

            out_data = unpack_data(decoded_data)
            data_dict.update(out_data)
            sleep(2)
            print(data_dict)
    except:
        print("Script interrompido")
        break