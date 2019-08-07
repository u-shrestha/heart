input_data = open("D:\Zzz Project\AAA practise\disease_prediction\prediction\heart.csv", "r").read().split("\n")
features = input_data[0].split(",")

del features[-1]
del input_data[0]
del input_data[-1]

samples = []
sample_classes = []

def cancer_enum(target):
	if target == 1:
		return 1
	else:
		return 0

def get_sample():
    for i, line in enumerate(input_data):
        data = line.split(",") #each data lai individual banako
        target = int(data[-1])
        del data[-1]
        samples.append(data)
        sample_classes.append(cancer_enum(target))
    return (samples, sample_classes)