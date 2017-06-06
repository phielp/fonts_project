import os
import csv
import re
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
from mmap import mmap,ACCESS_READ
from xlrd import open_workbook
import numpy as np
import glob

def extractXLS(path):
	for filename in glob.glob(os.path.join(path, '*.xls')):
		print(filename)
		os.makedirs(filename)

		new_file = open('../' + filename +'.csv', 'w')


path = '../Data/Test'

extractXLS(path)