import csv
import re
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import os
import glob

def drawLetter(pair, directory, name):
	scale = 4

	font_exceptions = [('arabic_msa', 'NotoNaskhArabic-Regular.ttf'), ('arabic_tunisian', 'NotoNaskhArabic-Regular.ttf'), 
		('arabic_turkic', 'NotoNaskhArabic-Regular.ttf'), ('armenian', 'NotoSerifArmenian-Regular.ttf'), 
		('assamese', 'NotoSansBengali-Regular.ttf'), ('avestan', 'NotoSansAvestan-Regular.ttf'), ('azeri', 'NotoNaskhArabic-Regular.ttf'), 
		('balti', 'NotoNaskhArabic-Regular.ttf'), ('beja', 'NotoNaskhArabic-Regular.ttf'), ('bengali', 'NotoSansBengali-Regular.ttf'), 
		('bhojpuri', 'NotoSansDevanagari-Regular.ttf'), ('brahmi', 'NotoSansBrahmi-Regular.ttf'), ('brahui', 'NotoNaskhArabic-Regular.ttf'), 
		('burmese', 'NotoSansMyanmar-Regular.ttf'), ('burushaski', 'NotoNaskhArabic-Regular.ttf'), ('carian', 'NotoSansCarian-Regular.ttf'), 
		('coptic', 'NotoSansCoptic-Regular.ttf'), ('cuneiform', 'NotoSansCuneiform-Regular.ttf'), ('dzongkha', 'NotoSansTibetan-Regular.ttf'), 
		('gothic', 'NotoSansGothic-Regular.ttf'), ('gujarati', 'NotoSansGujarati-Regular.ttf'), ('hebrew', 'NotoSansHebrew-Regular.ttf'), 
		('hindi', 'NotoSansDevanagari-Regular.ttf'), ('iranian', 'NotoNaskhArabic-Regular.ttf'), ('kannada', 'NotoSansKannada-Regular.ttf'), 
		('kashmiri', 'NotoNaskhArabic-Regular.ttf'), ('kayahli', 'NotoSansKayahLi-Regular.ttf'), ('khowar', 'NotoNaskhArabic-Regular.ttf'), 
		('korean', 'NotoSansCJKkr-Regular.otf'), ('lao', 'NotoSansLao-Regular.ttf'), ('lisu', 'NotoSansLisu-Regular.ttf'), 
		('lycian', 'NotoSansLycian-Regular.ttf'), ('lydian', 'NotoSansLydian-Regular.ttf'), ('magahi', 'NotoSansDevanagari-Regular.ttf'), 
		('maithili', 'NotoSansDevanagari-Regular.ttf'), ('malayalam', 'NotoSansMalayalam-Regular.ttf'), ('manchu', 'NotoSansMongolian-Regular.ttf'), 
		('mandaic', 'NotoSansMandaic-Regular.ttf'), ('manipuri', 'NotoSansBengali-Regular.ttf'), ('marathi', 'NotoSansDevanagari-Regular.ttf'), 
		('marwari', 'NotoSansDevanagari-Regular.ttf'), ('mongolic', 'NotoSansMongolian-Regular.ttf'), ('nepali', 'NotoSansDevanagari-Regular.ttf'), 
		('okinawan', 'NotoSansCJKjp-Regular.otf'), ('oriya', 'NotoSansOriya-Regular.ttf'), ('pali', 'NotoSansDevanagari-Regular.ttf'), 
		('phagspa', 'NotoSansPhagsPa-Regular.ttf'), ('punjabi', 'NotoNaskhArabic-Regular.ttf'), ('rejang', 'NotoSansRejang-Regular.ttf'), 
		('sanskrit', 'NotoSansDevanagari-Regular.ttf'), ('shan', 'NotoSansMyanmar-Regular.ttf'), ('sinhala', 'NotoSansSinhala-Regular.ttf'), 
		('somali', 'NotoNaskhArabic-Regular.ttf'), ('sundanese', 'NotoSansSundanese-Regular.ttf'), ('sylheti', 'NotoSansBengali-Regular.ttf'), 
		('syriac', 'NotoSansSyriacEastern-Regular.ttf'), ('tamil', 'NotoSansTamil-Regular.ttf'), ('telugu', 'NotoSansTelugu-Regular.ttf'), 
		('tengwar_arabic', 'NotoNaskhArabic-Regular.ttf'), ('thai', 'NotoSansThai-Regular.ttf'), ('tibetan', 'NotoSansTibetan-Regular.ttf'), 
		('tshangla', 'NotoSansTibetan-Regular.ttf'), ('tulu', 'NotoSansKannada-Regular.ttf'), ('adamaua', 'NotoNaskhArabic-Regular.ttf'), 
		('arakanese', 'NotoSansMyanmar-Regular.ttf'), ('arwi', 'NotoNaskhArabic-Regular.ttf'), ('avar', 'NotoNaskhArabic-Regular.ttf'), 
		('aynu', 'NotoNaskhArabic-Regular.ttf'), ('bisu', 'NotoSansMyanmar-Regular.ttf'), ('bosnian', 'NotoNaskhArabic-Regular.ttf'), 
		('chechen', 'NotoNaskhArabic-Regular.ttf'), ('fula', 'NotoNaskhArabic-Regular.ttf'), ('futhorc', 'BeorcGothicRegular.ttf'), 
		('hajong', 'NotoSansMyanmar-Regular.ttf'), ('javanese', 'NotoSansCJKtc-Regular.otf'), ('jeju', 'NotoSansCJKkr-Regular.otf'), 
		('kabyle', 'NotoNaskhArabic-Regular.ttf'), ('karen', 'NotoSansTibetan-Regular.ttf'), ('kumyk', 'NotoNaskhArabic-Regular.ttf'), 
		('kutchi', 'NotoSansDevanagari-Regular.ttf'), ('ladakhi', 'NotoSansTibetan-Regular.ttf'), ('latin_english', 'BeorcGothicRegular.ttf'), 
		('lontara', 'NotoSansBuginese-Regular.ttf'), ('mendekan', 'NotoNaskhArabic-Regular.ttf'), ('mro', 'NotoSansMyanmar-Regular.ttf'), 
		('nabataean', 'NotoSansImperialAramaic-Regular.ttf'), ('phagspa', 'NotoSansMongolian-Regular.ttf'), ('rohingya', 'NotoNaskhArabic-Regular.ttf'), 
		('sankethi', 'NotoSansTamil-Regular.ttf'), ('shina', 'NotoSansTibetan-Regular.ttf'), ('sikkimese', 'NotoSansTibetan-Regular.ttf'), 
		('sunuwar', 'NotoSansTibetan-Regular.ttf')]

	font_size = scale*6
	back_ground_color = (255, 255, 255, 255)
	font_color = (0, 0, 0, 255)
	unicode_text = pair[0]

	font_path = '../Data/Fonts/'

	base = Image.open('../Attachments/base.png').convert('RGBA')
	resized = base.resize((scale*16,scale*8))
	im = Image.new('RGBA',resized.size, back_ground_color)
	draw = ImageDraw.Draw(im)

	font_name = "NotoSans-Regular.ttf"
	for font in font_exceptions:
		if name == font[0]:
			font_name = font[1]
			
	font3 = ImageFont.truetype(font_path + font_name, font_size)
	draw.text((0,0), unicode_text, font = font3, fill = font_color)
	out = Image.alpha_composite(resized, im)

	converted = out.convert(mode='L')
	# converted.show()
	file_name = directory + '/png/' + unicode_text + '.png'
	converted.save(file_name)

	matrix = np.asarray(converted)
	return matrix

# new_file = open('../Data/Test/testFinal.csv', 'w')

path = '../Data/CSV/'

n_letters = 12

square = np.array([[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,227,227,227,227,227,227,227,227,227,227,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,0,0,0,0,0,0,0,0,0,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,0,205,243,243,243,243,243,243,205,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,0,215,255,255,255,255,255,255,215,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,0,215,255,255,255,255,255,255,215,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,0,215,255,255,255,255,255,255,215,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,0,215,255,255,255,255,255,255,215,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,0,215,255,255,255,255,255,255,215,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,0,215,255,255,255,255,255,255,215,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,0,215,255,255,255,255,255,255,215,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,0,215,255,255,255,255,255,255,215,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,0,215,255,255,255,255,255,255,215,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,0,215,255,255,255,255,255,255,215,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,0,215,255,255,255,255,255,255,215,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,0,215,255,255,255,255,255,255,215,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,0,215,255,255,255,255,255,255,215,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,0,182,215,215,215,215,215,215,182,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,0,0,0,0,0,0,0,0,0,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255]])

other_fonts = ['adamaua', 'arabic_msa', 'arabic_tunisian', 'arabic_turkic', 'arakanese', 'armenian', 'arwi', 'assamese', 'avar', 'avestan', 'aynu', 'azeri', 'balti', 'beja', 'bengali', 'bhojpuri', 'bisu', 'bosnian', 'brahmi', 'brahui', 'burmese', 'burushaski', 'carian', 'chechen', 'coptic', 'cuneiform', 'dzongkha', 'fula', 'futhorc', 'gothic', 'grantha', 'gujarati', 'hajong', 'hebrew', 'hindi', 'iranian', 'javanese', 'jeju', 'kabyle', 'kannada', 'karen', 'kashmiri', 'kayahli', 'khowar', 'korean', 'kumyk', 'kutchi', 'ladakhi', 'lao', 'latin_english', 'lisu', 'lontara', 'lycian', 'lydian', 'magahi', 'maithili', 'malayalam', 'manchu', 'mandaic', 'manipuri', 'marathi', 'marwari', 'mendekan', 'mongolic', 'mro', 'nabataean', 'nepali', 'okinawan', 'oriya', 'pali', 'phagspa', 'punjabi', 'rejang', 'rohingya', 'sankethi', 'sanskrit', 'shan', 'shina', 'sikkimese', 'sinhala', 'somali', 'sundanese', 'sunuwar', 'sylheti', 'syriac', 'tamil', 'telugu', 'tengwar_arabic', 'thai', 'tibetan', 'tshangla', 'tulu']

for filename in glob.glob(os.path.join(path, '*.csv')):
	name = filename[n_letters:-4]
	# print(name)
	directory = '../Data/Final/' + name

	if not os.path.exists(directory):
		os.makedirs(directory + '/png')
		os.makedirs(directory + '/csv')
	new_file_path = directory + '/' + name + '.csv'
	# print(new_file_path)
	new_file = open(new_file_path, 'w')

	with open(filename, 'r') as f:
		reader = csv.reader(f, delimiter = ',')
		for row in reader:
			if any(row):
				grapheme = row[0].lstrip()
				phoneme = row[-2]
				pair = (grapheme.split(' ')[0], phoneme)
				letter_name = pair[0].replace('/', '\\')
				pair = (letter_name, phoneme)
				# print(pair)
				new_file.write(pair[0] +  ', ' + pair[1] + '\n')
				table = drawLetter(pair, directory, name)

				if np.array_equal(table, square):
					print(name)

				letter_name = pair[0].replace('/', '_')
				file_name = os.path.join(directory + '/csv/' + pair[0] + '.csv')
				with open(file_name, 'w') as g:
					writer = csv.writer(g)
					writer.writerows(table.tolist())


	new_file.close()

	f.close()



	# 		# table = drawLetter(pair)
	# 		new_file.write(pair[0] +  ', ' + pair[1] + '\n')

	# 		file_name = '../Attachments/' + pair[0] + '.csv'

	# 		with open(file_name, 'w') as g:
	# 			writer = csv.writer(g)
	# 			writer.writerows(table.tolist())

	# 		# for i in range(0, int(np.sqrt(table.size))):
	# 		# 	print table[i]





