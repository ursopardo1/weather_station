from weather_function import unpack_data, decode_format, avg_list  # Função de unpack string -> dict
import serial
from time import sleep
import time
import csv
import datetime

today = datetime.date.today()

fileName = "analog_DHT.csv"
mcu_connection = 'COM8'  # ('/dev/ttyUSB1')
serial = serial.Serial(mcu_connection, 9600)
serial.flushInput()

avg_dict = {'Temperatura média: ': None, 'Umidade média: ': None, 'Luminosidade: ': None}
temp_data = []
umi_data = []
lumi_data = []

while True:
    try:
        # serial_data = serial.readline()
        serial.flushInput()
        try:
            for num in range(1, 10):

                """ Desenvolver função para leitura, unpacking e decoding """

                decoded_data = decode_format(serial.readline())
                working_data1 = unpack_data(decoded_data)
                temp_data.append(working_data1.get('Temperatura:'))  # Adiciona dado a lista para cálculo de média
                sleep(2)
                decoded_data = decode_format(serial.readline())
                working_data2 = unpack_data(decoded_data)
                umi_data.append(working_data2.get('Umidade:'))  # Adiciona dado a lista para cálculo de média
                sleep(2)
                decoded_data = decode_format(serial.readline())
                working_data3 = unpack_data(decoded_data)
                lumi_data.append(working_data3.get('Luminosidade:'))  # Adiciona dado a lista para cálculo de média
                # print(temp_data)
                # print(umi_data)
                sleep(360)  # Espera 6 minutos, em um range de 10 amostras, para cálculo da média

            print(f"Média Temperatura: {avg_list(temp_data)}")
            print(f"Média Umidade: {avg_list(umi_data)}")
            print(f"Média Luminosidade: {avg_list(lumi_data)}")
            avg_dict['Temperatura média: '] = avg_list(temp_data)
            avg_dict['Umidade média: '] = avg_list(umi_data)
            avg_dict['Luminosidade: '] = avg_list(lumi_data)
            print(avg_dict)
        except:
            continue
        with open(str(today)+'_data', "a") as f:  # Escreve a média de 10 amostras em 1 hora, com data e hora
            # f.write(data_dict)
            # f.write('\n')
            writer = csv.writer(f, delimiter=",")
            writer.writerow([time.asctime(), avg_dict])
        temp_data.clear()
        umi_data.clear()
    except:
        print("Script interrompido")
        break
