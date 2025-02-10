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

# importing tabular data into a script
data_p = pandas.read_csv("weather_data.csv")
# print(data_p)

# # isolating and printing a specific columns within our Data Frame.
# # print(data_p['temp'])

# # conversiting our data from from a tabular form to a dictionary.
# data_dict = data_p.to_dict()
# # print(data_dict)

# # i could also use the sum() method for iterables, or the mean() method in pandas
# # printing the average of all the temps within the temp column.
# #  total_temp = 0 
# # for temp in temp_list: 
# #     total_temp += temp
# # average_temp = total_temp/len(temp_list)
# # print(average_temp)

# # using the built in methods of panda to obtain the highest value within the temp column.
max_temp = data_p['temp'].max()
# print(max_temp)

# getting data that is within the rows of our entire data frame.
first_day = data_p[data_p.day == 'Monday']
# print(first_day)
 
# getting the row of data that had the highest temperature of the week. 
day_of_max_temp = data_p[data_p.temp == data_p.temp.max()]
# print(day_of_max_temp)

# isolating values within a rows that meets a specific condition
monday = data_p[data_p.day == "Monday"]
# print(monday.temp)
# print(monday.temp[0]) # removes the row number from the output.
# print((monday.temp[0])*(9/5) + 32)

#create a data from from scratch

data_dict  = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76,56,65]
}

data = pandas.DataFrame(data_dict)
data.to_csv('new_data.csv')
# print(data)