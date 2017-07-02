import os
import random

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def my_shuffle(array):
        random.shuffle(array)
        return array

directory = '../Data/Final/'
scripts = get_immediate_subdirectories(directory)

print(scripts)

characters = []        

def allCharacters():
	with open(directory + 'AllCharacters.csv', 'w') as f:
		for script in scripts:
			filename = directory + script + '/' + script + '_alt.csv'
			with open(filename, 'r') as g:
				for row in g:
					f.write(script + ',' + row)
				g.close()
		f.close()

allCharacters()



with open(directory + 'AllCharacters.csv', 'r') as f:
	for line in f:
		characters.append(line)
	print(len(characters))
	f.close()

train_percentage = 0.8
validation_percentage = 0.1
test_percentage = 0.1

total = len(characters)

train_abs = round(train_percentage * total)
validation_abs = round(validation_percentage * total)
test_abs = round(test_percentage * total)

validation_set = random.sample(characters, int(validation_abs))

for script in validation_set:
	del characters[characters.index(script)]

test_set = random.sample(characters, int(test_abs))

for script in test_set:
	del characters[characters.index(script)]

train_set = my_shuffle(characters)

print(len(test_set))
print(len(validation_set))
print(len(train_set))

with open(directory + 'RandomValidation.csv', 'w') as f:
	for line in validation_set:
		f.write(line)
	f.close()

with open(directory + 'RandomTest.csv', 'w') as f:
	for line in test_set:
		f.write(line)
	f.close()

with open(directory + 'RandomTrain.csv', 'w') as f:
	for line in train_set:
		f.write(line)
	f.close()



