import numpy as np
from sklearn import tree
from . import sample

class_names = ['yes', 'no']
samples, sample_classes = sample.get_sample()

clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(samples, sample_classes)


def predict(li):
	input_data = np.array(li).reshape(1, -1)
	result = clf.predict(input_data)
	print(result)
	if result == 0:
		return "false"
	else:
		return "true"