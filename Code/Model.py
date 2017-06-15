from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv1D, Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, Reshape
from keras import backend as K
import keras
import os
import csv
import glob
import numpy as np
import ast
# from keras import backend as K
# K.set_image_dim_ordering('th')

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def create_dataset(directory):
	train_data = []
	legend = []

	scripts = get_immediate_subdirectories(directory)

	for script in scripts:
		# csv look up table
		# get phonemes

		print script 		
		with open(directory + script + '/' + script + '_alt.csv', 'r') as f:
			reader = csv.reader(f, delimiter = ',')
			for row in reader:
				if any(row):

					new_row = ast.literal_eval(row[-1])
					legend.append(new_row)
					# print type(row[-1])
					# print type(new_row)
					# print(new_row)

					# get grapheme arrays
					path = directory + script + '/csv/' + row[0] + '.csv'
					# print(path + '/' + row[0] + '.csv')
					sample = np.genfromtxt(path, delimiter=',')
					# print sample
					train_data.append(sample.flatten())

	train_x = np.asarray(train_data)
	train_y = np.asarray(legend)
	return train_x, train_y

def create_dataset_alt(directory):
	train_data = []
	legend = []

	scripts = get_immediate_subdirectories(directory)

	for script in scripts:
		# csv look up table
		# get phonemes

		print script 		
		with open(directory + script + '/' + script + '_alt.csv', 'r') as f:
			reader = csv.reader(f, delimiter = ',')
			for row in reader:
				if any(row):

					new_row = ast.literal_eval(row[-1])
					legend.append(new_row)
					# print type(row[-1])
					# print type(new_row)
					# print(new_row)

					# get grapheme arrays
					path = directory + script + '/csv/' + row[0] + '.csv'
					# print(path + '/' + row[0] + '.csv')
					sample = np.genfromtxt(path, delimiter=',')
					# print sample
					train_data.append(sample)

	train_x = np.asarray(train_data)
	train_y = np.asarray(legend)
	return train_x, train_y

# paths to data
train_dir = '../Data/Train/'
test_dir= '../Data/Test/'

# Sequential Model
def sequential_model():
	# create test and train sets
	train_x, train_y = create_dataset(train_dir)
	test_x, test_y = create_dataset(test_dir)

	n_target_features = 10

	model = Sequential()
	model.add(Dense(n_target_features, activation='relu', input_shape=(2048,)))
	model.add(Dense(n_target_features, activation='softmax'))

	model.compile(optimizer='rmsprop',
	              loss='binary_crossentropy',
	              metrics=['accuracy'])


	model.fit(train_x, train_y, batch_size=16, epochs=10)
	score = model.evaluate(test_x, test_y, batch_size=16)
	print '\n', score


# CNN Model
def CNN_model():

	train_x, train_y = create_dataset_alt(test_dir)
	# test_x, test_y = create_dataset(test_dir)

	print train_x.shape

	n_target_features = 10

	img_cols, img_rows = 64, 32  # width, height


	# input_shape=(img_width, img_height, 1)
	# train_x = train_x.reshape(train_x.shape[0], 1, img_width, img_height)
	# train_y = train_y.reshape(train_y.shape[0], 1, img_width, img_height)

	model = Sequential()

	# model.add(Conv1D(n_target_features, 3, input_shape=(64, 32)))

	# conv layer 2D
	model.add(Reshape((1, img_rows, img_cols), input_shape=(2048,)))
	model.add(Conv2D(n_target_features, (3, 3), data_format='channels_last'))
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))

	# conv layer 2
	# model.add(Conv2D(n_target_features, (3, 3), padding='same'))
	# model.add(Activation('relu'))
	# model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))

	# model.add(Flatten())
	# model.add(Dense(64))
	# model.add(Activation('relu'))
	# model.add(Dropout(0.5))
	# model.add(Dense(1))
	# model.add(Activation('sigmoid'))

	model.compile(optimizer='rmsprop',
	              loss='binary_crossentropy',
	              metrics=['accuracy'])

	model.fit(train_x, train_y, batch_size=16, epochs=10)



# sequential_model()
CNN_model()
