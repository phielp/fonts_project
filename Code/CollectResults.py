import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm 
import statistics


features = ['approximant_acc', 'approximant_loss', 'back_acc', 'back_loss', 'consonantal_acc', 
'consonantal_loss', 'continuant_acc', 'continuant_loss', 'delayedrelease_acc', 
'delayedrelease_loss', 'front_acc', 'front_loss', 'height_acc', 'height_loss', 
'labial_acc', 'labial_loss', 'loss', 'low_acc', 'low_loss', 'nasal_acc', 'nasal_loss', 
'round_acc', 'round_loss', 'sonorant_acc', 'sonorant_loss', 'strident_acc', 'strident_loss', 
'tense_acc', 'tense_loss']

file_path1 = '../Data/Results/TwoLayerModelResults.csv'
file_path2 = '../Data/Results/ThreeLayerModelResults.csv'
file_path3 = '../Data/Results/TwoLayerModelRandomResults.csv'
file_path4 = '../Data/Results/ThreeLayerModelRandomResults.csv'

def resultsDict(file_path):
	feature_dict = {}

	for feature in features:
		feature_dict[feature] = []
	with open(file_path, 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			if any(row):
				if row[0] in feature_dict:
					temp = feature_dict[row[0]]
					temp.append(float(row[1]))

					feature_dict[row[0]] = temp # + float(row[1])

	return feature_dict



dict1 = resultsDict(file_path1)
dict2 = resultsDict(file_path2)
dict3 = resultsDict(file_path3)
dict4 = resultsDict(file_path4)

print('%.4f' % statistics.median(dict1['loss']))
print('%.4f' % statistics.median(dict2['loss']))
print('%.4f' % statistics.median(dict3['loss']))
print('%.4f' % statistics.median(dict4['loss']))

# for key, value in dict1.items():

# 	model1_result = '%.4f' % float(value / 10)
# 	model2_result = '%.4f' % float(dict2[key] / 10)
# 	model3_result = '%.4f' % float(dict3[key] / 10)
# 	model4_result = '%.4f' % float(dict4[key] / 10)

# 	print key + ' & ' + str(model1_result) + ' & ' + str(model2_result) + ' & ' + str(model3_result) + ' & ' + str(model4_result) + ' \\\\'

# plt.figure()
# plt.subplot(1,2,1)
# plt.title('loss_total')
# plt.xlabel('run')
# plt.ylabel('value')
# plt.plot(dict1['loss'], 'ro', color = 'r', label = "Two Layer Model")
# plt.plot(dict2['loss'], 'x', color = 'b', label = "Three Layer Model")
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# plt.savefig('../Data/Plots/loss_total.png')
# plt.show()

# for font in fm.findSystemFonts():
#     print font



