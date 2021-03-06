import requests
import traceback
import time
import sys
from lxml import html
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import datetime
import numpy as np

def graphInfo():
	# get webpage
	url = 'http://www.graphemica.com/1000'
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	page = requests.get(url, headers=headers)

	# parse webpage
	root = html.document_fromstring(page.text)
	header = root.xpath('/html/body/div[3]/article/header')
	table = root.xpath('/html/body/div[3]/article/section[1]/section/table')[0].findall('tr')
	# table2 = root.xpath('/html/body/div[3]/article/section[4]/section[3]/table')[0].findall('tr')

	# assign info
	grapheme = header[0][0].text
	script =  table[1][1].text_content()
	uniCode = table[0][1].text_content()

	print grapheme, script, uniCode

def drawLetter():
	scale = 4

	font_size = scale*6
	back_ground_color = (255, 255, 255, 255)
	font_color = (0, 0, 0, 255)
	unicode_text = u'\u0414'
	print unicode_text
	# \u1001\u1002\u1003\u1040
	# unicode_text = u'[ k\u02b0\xe1 ]'

	# NotoSansMyanmar-Regular.ttf
	# FreeSans.ttf
	# unifont-9.0.06.ttf
	font_path = '../Noto-unhinted/'

	base = Image.open('base.png').convert('RGBA')
	resized = base.resize((scale*8,scale*8))
	im = Image.new('RGBA',resized.size, back_ground_color)
	draw = ImageDraw.Draw(im)
	font1 = ImageFont.truetype("NotoSansMyanmar-Regular.ttf", font_size)
	font2 = ImageFont.truetype("unifont-9.0.06.ttf", font_size)
	font3 = ImageFont.truetype(font_path + "NotoSans-Regular.ttf", font_size)
	# font4 = ImageFont.load_default().font
	draw.text((0,0), unicode_text, font = font3, fill = font_color)
	# draw.text((10,80), unicode_text, font = font2, fill = font_color)
	# draw.text((10,160), unicode_text.encode('utf8'), font = font3, fill = font_color)
	out = Image.alpha_composite(resized, im)
	converted = out.convert(mode='L')
	converted.show()
	# converted.save('letter.png')

	matrix = np.asarray(converted)
	return matrix

table = drawLetter();
for i in range(0, int(np.sqrt(table.size))):
	print table[i]

