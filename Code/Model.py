from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, Model
from keras.layers import Conv1D, Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, Reshape, Input
from keras.utils import np_utils, plot_model
from keras import backend as K
from sklearn.preprocessing import LabelEncoder
import keras
import os
import csv
import glob
import numpy as np
import ast

train_set = ['abaza', 'abenaki', 'abkhaz', 'acehnese', 'acheron', 'acholi', 
    'achuar-shiwiar', 'adamaua', 'adzera', 'afar', 'afrikaans', 'aghul', 
    'aguaruna', 'akan', 'akhvakh', 'aklan', 'akurio', 'alabama', 'alsatian', 
    'alur', 'amahuaca', 'amarakaeri', 'andi', 'andoa', 'anuki', 'apache', 
    'arabic_cypriot', 'arabic_msa', 'arabic_tunisian', 'arakanese', 'araki', 
    'aranese', 'arapaho', 'archi', 'are', 'arikara', 'armenian', 'arvanitic', 
    'arwi', 'ashaninka', 'asheninka', 'assamese', 'asturian', 'atlantean', 
    'avestan', 'avokaya', 'aynu', 'bagvalal', 'balti', 'bambara', 'bandial', 
    'basque', 'beja', 'bench', 'bengali', 'bhojpuri', 'bislama', 'bisu', 'bora', 
    'bouyei', 'brahmi', 'brahui', 'burmese', 'busa', 'caddo', 'capeverdeancreole', 
    'caquinte', 'carian', 'cayuga', 'chapalaa', 'chavacano', 'chechen', 'chickasaw', 
    'chilcotin', 'chipewyan', 'chuukese', 'cofan', 'cuneiform', 'cyrillic_finnougaric', 
    'cyrillic_other', 'cyrillic_romance', 'cyrillic_russian', 'cyrillic_slavic', 
    'cyrillic_tungusic', 'cyrillic_turkic', 'dagaare', 'danish', 'delaware', 'dutch', 
    'dzongkha', 'eskimo-aleut', 'estonian', 'ewondo', 'eyak', 'fijihindi', 'fula', 
    'futhorc', 'gitxsan', 'glagolitic', 'gothic', 'guineabissaucreole', 'gujarati', 
    'hajong', 'hebrew', 'hindi', 'indonesian', 'interlingua', 'ipa', 'iroquoian', 
    'kabyle', 'karachay-balkar', 'karen', 'kashmiri', 'kharosthi', 'khojki', 
    'khowar', 'korean', 'kove', 'kulitan', 'kumyk', 'kutchi', 'ladakhi', 'lao', 
    'latin_africa', 'latin_afroasiatic', 'latin_austroasiatic', 'latin_austronesian', 
    'latin_camerica', 'latin_celtic', 'latin_creoles', 'latin_finnougaric', 'latin_formosan', 
    'latin_germanic', 'latin_hmongmien', 'latin_italic', 'latin_khoisan', 
    'latin_namerica', 'latin_nilosaharan', 'latin_samerica', 'latin_slavonic', 
    'latin_taikaidai', 'latin_tng', 'latin_turkic', 'latvian', 'lithuanian', 
    'lokoya', 'loma', 'lontara', 'lopit', 'lycian', 'magahi', 'malay', 'malayalam', 
    'maltese', 'manchu', 'mandaic', 'mandarin', 'marathi', 'marwari', 'maskelynes', 
    'mato', 'mayan', 'mende', 'mendekan', 'mongolic', 'monkhmer', 'mro', 'mutsun', 
    'nabataean', 'nadene', 'nepali', 'nheengatu', 'ocs', 'okinawan', 'oriya', 
    'oromo', 'pali', 'pawnee', 'phagspa', 'pomoan', 'punjabi', 'quechuan', 
    'rarotongan', 'rejang', 'rohingya', 'romani', 'rovas', 'sankethi', 'sanskrit', 
    'shan', 'siar', 'sikaiana', 'sinhala', 'sinitic', 'somali', 'sundanese', 
    'sylheti', 'syriac', 'tami', 'tamil', 'tengwar_arabic', 'tengwar_icelandic', 
    'tengwar_welsh', 'thai', 'tibetan', 'tokipona', 'tongan', 'tsakonian', 'tshangla', 
    'tulu', 'tuvaluan', 'uto-aztecan', 'wandamen', 'wichita', 'wolof', 'yabem', 'zigula']
validation_set = ['makonde', 'telugu', 'lisu', 'shina', 'maithili', 'borgu', 
    'degxinag', 'kannada', 'bedik', 'avar', 'iranian', 'babine', 'kayahli', 
    'albanian', 'sikkimese', 'caucasian', 'manipuri', 'badaga', 'latin_ial', 
    'arawakan', 'anutan', 'menominee', 'bosnian', 'griko', 'teiwa', 'comox', 
    'latin_english']
test_set = ['latin_aboriginal', 'arabic_turkic', 'khmer', 'philippine', 'comorian', 
    'lydian', 'ubykh', 'arabela', 'burushaski', 'latgalian', 'coptic', 'sio', 'westernrote', 
    'jeju', 'awing', 'altay', 'grantha', 'lote', 'catalan', 'aymara', 'aromanian', 'azeri', 
    'bushi', 'salishan', 'javanese', 'beaver', 'sunuwar']

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

def create_dataset_final(set_name):
    directory = '../Data/Final/'

    train_data = []
    legend = []

    scripts = set_name

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
validation_dir = '../Data/Validation/'

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
    train_x, train_y = create_dataset_final(train_set)
    print "shape trainX:", train_x.shape
    print "shape trainY:", train_y.shape
    test_x , test_y = create_dataset_final(test_set)
    print "shape testX:", test_x.shape
    print "shape testY:", test_y.shape
    validation_x, validation_y = create_dataset_final(validation_set)
    print "shape validationX:", validation_x.shape
    print "shape validationY:", validation_y.shape

    # train_x, train_y = create_dataset_alt(train_dir)
    # print "shape trainX:", train_x.shape
    # print "shape trainY:", train_y.shape
    # test_x , test_y = create_dataset_alt(test_dir)
    # print "shape testX:", test_x.shape
    # print "shape testY:", test_y.shape
    # validation_x, validation_y = create_dataset_alt(validation_dir)
    # print "shape validationX:", validation_x.shape
    # print "shape validationY:", validation_y.shape

    n_target_features = 3

    train_targets = individual_feature(train_y, 14)
    test_targets = individual_feature(test_y, 14)
    validation_targets = individual_feature(validation_y, 14)

    img_cols, img_rows = 64, 32  # width, height

    # create model
    inputs = Input(shape=(img_rows, img_cols,))

    reshaped = Reshape((1, img_rows, img_cols), input_shape=(32,64))(inputs)

    conv1 = Conv2D(n_target_features, kernel_size=(9, 9), activation='relu', data_format='channels_first')(reshaped)
    max_pool1 = MaxPooling2D(pool_size=(2, 2), padding ='same')(conv1)

    # conv layer 2
    conv2 = Conv2D(n_target_features, kernel_size=(3, 3), activation='relu', padding='same')(max_pool1)
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

    # top_k_categorical_accuracy()

    model.compile(optimizer='rmsprop',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    predictions = model.predict(train_x)[0]

    model.fit(train_x, train_targets, batch_size=16, epochs=10, 
        validation_data = (validation_x, validation_targets))
    score = model.evaluate(test_x, test_targets, batch_size=16)
    print "\n score: ", score
    plot_model(model, to_file = '../Data/Plots/model.png', show_shapes = True)

# sequential_model()
# CNN_sequential()
if __name__ == '__main__':
    CNN_model()








