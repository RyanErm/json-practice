#!/usr/bin/python3


#import neccessary packages
import json
#load in the json file
with open('chacon.json', 'r') as file:
	data = json.load(file)

#clear out the file
with open('chacon.csv', 'w') as file:
	file.write('')
for i in range(0,5):
	#loop through the first five entries and get the specified fields
	with open('chacon.csv', 'a') as file:
		file.write(data[i]['name'])
		file.write(',')
		file.write(data[i]['html_url'])
		file.write(',')
		file.write(data[i]['updated_at'])
		file.write(',')
		file.write(data[i]['visibility'])
		file.write("\n")
