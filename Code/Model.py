from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import keras
import os
import csv
import glob
import numpy as np

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

directory = '../Data/CSVTest/'
scripts = get_immediate_subdirectories(directory)

train_data = []
legend = []

for script in scripts:

	# csv look up table
	# get phonemes
	with open(directory + script + '/' + script +'.csv', 'r') as f:
		reader = csv.reader(f, delimiter = ',')
		for row in reader:
			if any(row):

				legend.append(row[-1].lstrip())

	# get grapheme arrays
	path = directory + script + '/csv'
	for filename in os.listdir(path):
		# print(path + '/' + filename)
		sample = np.genfromtxt(path + '/' + filename, delimiter=',')

		train_data.append(sample.flatten())

img_width, img_height = 64, 32

model = Sequential()
model.add(Dense(32, activation='relu', input_shape=(2048,)))
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

data = np.asarray(train_data)
labels = np.asarray(legend)

print data.shape
print labels.shape

# for i in range(0, labels.size):
# 	print labels[i]

one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)


