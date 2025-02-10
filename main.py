# import csv #built in python module

# with open(file='weather_data.csv') as file:
#     data = file.readlines()
#     print(data)

# import csv 

# with open(file='weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     count = 0 
#     for row in data:
#         if row[1] != 'temp':
#            temperature.append(int(row[1]))
#     print(temperature)


import pandas

data_p = pandas.read_csv("weather_data.csv")
# print(data_p)
# print(data_p['temp'])

data_dict = data_p.to_dict()
# print(data_dict)

data_list = data_p['temp'].to_list()
print(data_list)

total_temp = 0 
for temp in data_list: 
    total_temp += temp
average_temp = total_temp/len(data_list)
print(average_temp)