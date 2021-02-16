## from weather_function import unpack_data # Função de unpack string -> dict
import serial
from time import sleep, time
import csv


serial = serial.Serial('/dev/ttyUSB1')
serial.flushInput()

data_dict = {}

while True:
    try:
        serial_data = serial.readline()
        decoded_data = serial_data.decode("utf-8")
        # print(decoded_data)
        with open("w_data", "a") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow([time.time(), decoded_data])

        ## out_data = unpack_data(decoded_data)
        ## data_dict.update(out_data)
        sleep(2.1)
        ## print(data_dict)
    except:
        print("Script interrompido")
        break