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


print(len(conversions))
print(type(conversions))
uniques = []
for key, value in conversions.items():
	uniques.append(value)

uniques = list(set(uniques))

# replace with random feature vecs (phonological encoding scheme)
for index , unique in enumerate(uniques):
	feature_vec = create_random_vec(0, 10)
	uniques[index] = (unique, feature_vec)

for key, value in conversions.items():
	for unique in uniques:
		# print(unique[0])
		if value == unique[0]:
			conversions.update({key : unique[1]})

print(conversions)

# get names of sub directories
def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
	
def replace_IPAsymbols():
	# parse csv files in sub dirs and store conversions in new csv file
	for script in scripts:
		print(script)
		# read old csv
		with open(directory + script + '/' + script +'.csv', 'r') as f:
			reader = csv.reader(f, delimiter = ',')

			# write to new 'name_alt.csv'
			with open(directory + script + '/' + script +'_alt.csv', 'w', newline='') as g:
				writer = csv.writer(g)

				for row in reader:
					if any(row):
						IPAsymbol = row[1].lstrip()
						for old, new in conversions.items():
							if old == IPAsymbol[1:-1]:
								# print(new)
								writer.writerow([row[0], new])
							# else:
							# 	writer.writerow([row[0], IPAsymbol[1:-1]])


directory = '../Data/Train/'
scripts = get_immediate_subdirectories(directory)
replace_IPAsymbols()				