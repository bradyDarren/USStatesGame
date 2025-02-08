# import csv #built in python module

# with open(file='weather_data.csv') as file:
#     data = file.readlines()
#     print(data)

import csv 

with open(file='weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperature = []
    count = 0 
    for row in data:
        if row[1] != 'temp':
           temperature.append(int(row[1]))
    print(temperature)
