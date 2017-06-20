import os
import random

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

directory = '../Data/Final/'
scripts = get_immediate_subdirectories(directory)

train_percentage = 0.8
validation_percentage = 0.1
test_percentage = 0.1

total = len(scripts)

train_abs = round(train_percentage * total)
validation_abs = round(validation_percentage * total)
test_abs = round(test_percentage * total)

validation_set = random.sample(scripts, int(validation_abs))

for script in validation_set:
	del scripts[scripts.index(script)]

test_set = random.sample(scripts, int(test_abs))

for script in test_set:
	del scripts[scripts.index(script)]

train_set = scripts

print train_set, validation_set, test_set
