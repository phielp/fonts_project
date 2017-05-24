import csv
import re
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

def drawLetter(pair):
	scale = 4

	font_size = scale*6
	back_ground_color = (255, 255, 255, 255)
	font_color = (0, 0, 0, 255)
	unicode_text = pair[0]

	font_path = '../Data/Fonts/'

	base = Image.open('../Attachments/base.png').convert('RGBA')
	resized = base.resize((scale*16,scale*8))
	im = Image.new('RGBA',resized.size, back_ground_color)
	draw = ImageDraw.Draw(im)

	font3 = ImageFont.truetype(font_path + "NotoSans-Regular.ttf", font_size)
	draw.text((0,0), unicode_text, font = font3, fill = font_color)
	out = Image.alpha_composite(resized, im)

	converted = out.convert(mode='L')
	# converted.show()
	file_name = '../Attachments/' + unicode_text + '.png'
	converted.save(file_name)

	matrix = np.asarray(converted)
	return matrix

new_file = open('../Data/Test/testFinal.csv', 'w')

with open('../Data/Test/test.csv', 'r') as f:
	reader = csv.reader(f, delimiter = ',')
	for row in reader:
		grapheme = row[0]
		phoneme = row[-2]
		pair = (grapheme.split(' ')[0], phoneme)
		table = drawLetter(pair)
		new_file.write(pair[0] +  ', ' + pair[1] + '\n')

		file_name = '../Attachments/' + pair[0] + '.csv'

		with open(file_name, 'w') as g:
			writer = csv.writer(g)
			writer.writerows(table.tolist())

		# for i in range(0, int(np.sqrt(table.size))):
		# 	print table[i]





