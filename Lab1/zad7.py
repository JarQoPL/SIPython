import csv
import pandas as pd
# #load the csv file
# weatherFile = open('cereal.csv')
# #read the csv file into memory
# weatherReader = csv.reader(weatherFile)
# #convert csv data into a python list
# weatherList = list(weatherReader)
# print(weatherList)


df = pd.read_csv('cereal.csv')
saved_column = df.name
res = type(saved_column)
print(f" {saved_column} a typ to {res} ")
