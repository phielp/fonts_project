import csv
import os
import glob
import numpy as np
import random
import ast

# replace with random feature vecs (phonological encoding scheme)
# for index , unique in enumerate(uniques):
# 	feature_vec = create_random_vec(0, 10)
# 	uniques[index] = (unique, feature_vec)

# for key, value in conversions.items():
# 	for unique in uniques:
# 		# print(unique[0])
# 		if value == unique[0]:
# 			conversions.update({key : unique[1]})

conversions = {}
for key, value in csv.reader(open("../Data/IPAfeatures/output.csv")):
	conversions[key] = value

# print(conversions) 

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
						if '/' in IPAsymbol:
							choices = IPAsymbol[1:-1].split('/')
							# print(choices[1])
							for choice in choices:
								for old, new in conversions.items():
									if old == choice and len(new) > 10:
										writer.writerow([row[0], new])
						for old, new in conversions.items():
							if old == IPAsymbol[1:-1] and len(new) > 10:
								writer.writerow([row[0], new])
															
directory = '../Data/Final/'
scripts = get_immediate_subdirectories(directory)
replace_IPAsymbols()				