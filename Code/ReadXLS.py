from mmap import mmap,ACCESS_READ
from xlrd import open_workbook
import numpy as np
import glob
import os
import csv

path = '../Data/Test'

for filename in glob.glob(os.path.join(path, '*.xls')):
	print filename

	new_path = filename[:-4] + '.csv'

	new_file = open(new_path, 'w')

	# open .xls as workbook
	book = open_workbook(filename)
	# get first page
	print book.nsheets
	print book.sheet_names()

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
	words = ['consonants', 'vowels', 'vowels', 'diphthongs', 'other', 'letter', 
		'combination', 'diacritic', 'numeral', 'indication', 'devanagari', 'digraphs',
		'tone', 'text', 'only', 'foreign', 'kriol', 'pronunciation', 'series', 'alphabet',
		'yale', 'romanization', 'initials', 'rimes', 'mutations']

	# format and store in .csv
	# new_file.write(filename + '\n')

	for j in range(table.shape[1]-1):
		for i in range(table.shape[0]):
			value = table[i][j]
			# replace filter words with _
			# for word in words:
			# 	if value.strip().lower() == word:
			if any(word in value.strip().lower() for word in words):
				value = '_'
			if '_' not in value:
				# store as readable
				new_file.write(value.encode('utf8') + ',')

				# store as Unicode encoding
				# new_file.write(repr(value) + ',')
			if '[' in value:
				new_file.write('\n')

	new_file.close()


# # reverse order
# new_file_rev = open('combinedRev.csv', 'w')

# with open('combined.csv', 'r') as textfile:
#     for row in reversed(list(csv.reader(textfile))):
#         new_file_rev.write(', '.join(row) + '\n')


