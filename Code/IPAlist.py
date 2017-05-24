import csv
import re

symbols = open('../Data/Final/combined.csv', 'r')

uniques = []

# extract IPA symbols
for symbol in symbols:
	uniCode = re.findall(r'\[.{1,5}\]', symbol)
	for i in range(0, len(uniCode)):
		symbolIPA = uniCode[i]
		if symbolIPA not in uniques:
			uniques.append(symbolIPA)

# print and write to file
new_file = open('IPAsymbols.txt', 'w')

for i in range(0, len(uniques)):
	print uniques[i]
	new_file.write(uniques[i] + '\n')

