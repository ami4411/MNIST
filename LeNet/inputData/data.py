from tensorflow import keras

import sys
import os

from inference.load import *
from inputData.process_data import *

def get_data():
	"""Get data from source and return raw data."""
	
	(train_x, train_y), (test_x, test_y) = keras.datasets.mnist.load_data()
	test_y = None

	return test_x, test_y

def select_process(chosen):

	data, label = get_data()

	clean_data = { 
	"1": Data.normalize_data(data),
	"2": Data.center_data(data),
	"3": Data.standardize_data(data)
	}

	fresult = Data.process_data(clean_data[chosen])
	pred = Predict(fresult, label)
	fpred = pred.predict()
	print(fpred)

	return fpred
