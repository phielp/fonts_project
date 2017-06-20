from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, Model
from keras.layers import Conv1D, Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, Reshape, Input
from keras.utils import np_utils
from keras import backend as K
from sklearn.preprocessing import LabelEncoder
import keras
import os
import csv
import glob
import numpy as np
import ast

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

        with open(directory + script + '/' + script + '_alt.csv', 'r') as f:
            reader = csv.reader(f, delimiter = ',')
            for row in reader:
                if any(row):

                    new_row = ast.literal_eval(row[-1])
                    legend.append(new_row)

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

        with open(directory + script + '/' + script + '_alt.csv', 'r') as f:
            reader = csv.reader(f, delimiter = ',')
            for row in reader:
                if any(row):

                    new_row = ast.literal_eval(row[-1])
                    legend.append(new_row)

                    # get grapheme arrays
                    path = directory + script + '/csv/' + row[0] + '.csv'
                    # print(path + '/' + row[0] + '.csv')
                    sample = np.genfromtxt(path, delimiter=',')
                    # print sample
                    train_data.append(sample)

    train_x = np.asarray(train_data)
    train_y = np.asarray(legend)
    return train_x, train_y

# returns one-hot encoding for 1 feature
def individual_feature(Y, n_features):
    final = []
    for n in range(0, n_features):
        feature_vec = []
        for y in Y:
            feature_vec.append([y[n]])
        final.append(np.array(feature_vec))
        # final.append(np_utils.to_categorical(feature_vec, num_classes = 4))
    return final

# paths to data
train_dir = '../Data/Train/'
test_dir = '../Data/Test/'

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
def CNN_sequential():

    train_x, train_y = create_dataset_alt(train_dir)
    print "shape trainX:", train_x.shape
    print "shape trainY:", train_y.shape

    test_x , test_y = create_dataset_alt(test_dir)
    print "shape testX:", test_x.shape
    print "shape testY:", test_y.shape

    n_target_features = 14

    img_cols, img_rows = 64, 32  # width, height

    model = Sequential()

    # adjust input shape
    model.add(Reshape((1, img_rows, img_cols), input_shape=(32,64)))
    # conv layer 2D
    model.add(Conv2D(n_target_features, kernel_size=(3, 3), activation='relu', data_format='channels_first'))
    # model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # conv layer 2
    model.add(Conv2D(n_target_features, kernel_size=(3, 3), activation='relu', padding='same'))
    # model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))

    model.add(Flatten())
    # model.add(Dense(64, activation='relu'))
    # model.add(Dropout(0.5))
    model.add(Dense(14, activation='sigmoid'))

    model.compile(optimizer='rmsprop',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])


    model.fit(train_x, train_y, batch_size=16, epochs=10)
    score = model.evaluate(test_x, test_y, batch_size=16)
    print '\n', score

def CNN_model():
    train_x, train_y = create_dataset_alt(train_dir)
    print "shape trainX:", train_x.shape
    print "shape trainY:", train_y.shape
    test_x , test_y = create_dataset_alt(test_dir)
    print "shape testX:", test_x.shape
    print "shape testY:", test_y.shape

    n_target_features = 4

    train_targets = individual_feature(train_y, 14)
    test_targets = individual_feature(test_y, 14)

    img_cols, img_rows = 64, 32  # width, height

    # create model
    inputs = Input(shape=(img_rows, img_cols,))

    reshaped = Reshape((1, img_rows, img_cols), input_shape=(32,64))(inputs)

    conv1 = Conv2D(n_target_features, kernel_size=(3, 3), activation='relu', data_format='channels_first')(reshaped)
    # max_pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

    # conv layer 2
    conv2 = Conv2D(n_target_features, kernel_size=(3, 3), activation='relu', padding='same')(conv1)
    max_pool2 = MaxPooling2D(pool_size=(2, 2), padding='same')(conv2)

    flatten = Flatten()(max_pool2)

    consonantal = Dense(n_target_features, activation='softmax', name='consonantal')(flatten)
    sonorant = Dense(n_target_features, activation='softmax', name='sonorant')(flatten)
    continuant = Dense(n_target_features, activation='softmax', name='continuant')(flatten)
    delayedRelease = Dense(n_target_features, activation='softmax', name='delayedrelease')(flatten)
    approximant = Dense(n_target_features, activation='softmax', name='approximant')(flatten)
    nasal = Dense(n_target_features, activation='softmax', name='nasal')(flatten)
    labial = Dense(n_target_features, activation='softmax', name='labial')(flatten)
    rounded = Dense(n_target_features, activation='softmax', name='round')(flatten)
    strident = Dense(n_target_features, activation='softmax', name='strident')(flatten)
    height = Dense(n_target_features, activation='softmax', name='height')(flatten)
    low = Dense(n_target_features, activation='softmax', name='low')(flatten)
    front = Dense(n_target_features, activation='softmax', name='front')(flatten)
    back = Dense(n_target_features, activation='softmax', name='back')(flatten)
    tense = Dense(n_target_features, activation='softmax', name='tense')(flatten)

    predictions = [consonantal, sonorant, continuant, delayedRelease, approximant, 
                   nasal, labial, rounded, strident, height, low, front, back, tense]

    model = Model(inputs=inputs, outputs=predictions)

    model.compile(optimizer='rmsprop',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    predictions = model.predict(train_x)[0]

    model.fit(train_x, train_targets, batch_size=16, epochs=10)
    score = model.evaluate(test_x, test_targets, batch_size=16)
    print '\n', score

# sequential_model()
# CNN_sequential()
if __name__ == '__main__':
    CNN_model()








