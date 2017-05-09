from mmap import mmap,ACCESS_READ
from xlrd import open_workbook
import numpy as np
import glob
import os
import csv

new_file = open('combined.csv', 'w')
path = '../Data/'

for filename in glob.glob(os.path.join(path, '*.xls')):
	print filename

	# open .xls as workbook
	book = open_workbook(path + filename)
	# get first page
	s = book.sheet_by_index(0)

	table = np.zeros((s.nrows,s.ncols), dtype=np.object)

	# copy values to table
	for row in range(s.nrows):
	    for col in range(s.ncols):
	    	
	    	if s.cell(row,col).ctype == 1:
	    		table[row][col] = s.cell(row,col).value

	    	# replace empty cells with: _
	    	else:
	    		table[row][col] = '_'

	# filter common words
	words = ['consonants', 'vowels', 'vowels & diphthongs', 'other letters']

	# format and store in .csv
	new_file.write(filename + '\n')

	for j in range(table.shape[1]):
		for i in range(table.shape[0]):
			value = table[i][j]
			# replace filter words with _
			for word in words:
				if value.strip().lower() == word:
					value = '_'
			if '_' not in value:
				# store as readable
				new_file.write(value.encode('utf8') + ',')

				# store as Unicode encoding
				new_file.write(repr(value) + ',')
			if '[' in value:
				new_file.write('\n')

	new_file.write('\n')


new_file.close()

# reverse order
new_file_rev = open('combinedRev.csv', 'w')

with open('combined.csv', 'r') as textfile:
    for row in reversed(list(csv.reader(textfile))):
        new_file_rev.write(', '.join(row) + '\n')


