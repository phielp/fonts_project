import csv
import os
import glob
import numpy as np
import random

# create dictionary with conversions from 'IPASegsUTF8.txt'
file_name = '../Data/IPAfeatures/IPASegsUTF8.txt'
conversions = {}

with open(file_name, 'r') as f:
	reader = csv.reader(f, delimiter = '\t')
	for row in reader:
		conversions.update({row[0] : row[1]})

f.close()

def create_random_vec(n, m):
	feature_vec = []
	print(type(feature_vec))
	for x in range(n, m):
		feature_vec.append(random.randrange(2))
	return feature_vec

def replace_value(value):
	if value == '-':
		return 0
	elif value == '+':
		return 1
	elif value == '0':
		return 2
	else:
		return 3

print(len(conversions))
print(type(conversions))
uniques = []
for key, value in conversions.items():
	uniques.append(value)

uniques = list(set(uniques))

final_segments = '../Data/IPAfeatures/segments_final.txt'

for key, value in conversions.items():
	with open(final_segments, 'r') as f:
		reader = csv.reader(f, delimiter = ',')
		for row in reader:
			if row[4] == value:
				feature_vec = []
				feature_vec.append(replace_value(row[16]))
				feature_vec.append(replace_value(row[17]))
				feature_vec.append(replace_value(row[18]))
				feature_vec.append(replace_value(row[19]))
				feature_vec.append(replace_value(row[20]))
				feature_vec.append(replace_value(row[22]))
				feature_vec.append(replace_value(row[24]))
				feature_vec.append(replace_value(row[25]))
				feature_vec.append(replace_value(row[30]))
				feature_vec.append(replace_value(row[32]))
				feature_vec.append(replace_value(row[33]))
				feature_vec.append(replace_value(row[34]))
				feature_vec.append(replace_value(row[35]))
				feature_vec.append(replace_value(row[36]))
				# print(value)
				print(row[4])
				print(feature_vec)
				conversions.update({key : feature_vec})
				break
	f.close()

print(conversions)

w = csv.writer(open("../Data/IPAfeatures/output.csv", "w"))
for key, val in conversions.items():
    w.writerow([key, val])