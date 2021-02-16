from weather_function import unpack_data # Função de unpack string -> dict
import serial
from time import sleep
import time
import csv


serial = serial.Serial('/dev/ttyUSB1')
serial.flushInput()

data_dict = {}
data_media = {}

while True:
    try:
        serial_data = serial.readline()
        try:
            for num in range(1, 3):
                decoded_data = serial_data.decode("utf-8")
                out_data = unpack_data(decoded_data)
                data_dict.update(out_data)
                sleep(2)
                print(data_dict)
        except:
            continue
        with open("w_data", "a") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow([time.time(), data_dict])
    except:
        print("Script interrompido")
        break