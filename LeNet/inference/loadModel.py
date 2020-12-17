import tensorflow as tf
from tensorflow import keras
from sklearn.datasets import load_digits
from skimage.transform import resize

import numpy as np

import os
import sys

class Predict:

	def __init__(self, test):
		self.test = test

	@staticmethod
	def get_model():

		try:
			pathResult = os.chdir("saved")
			print("Path changed:", os.getcwd())
		except:
			print("Path not found:", sys.exc_info())

		fileName = [int(fileDate) for fileDate in os.listdir()]
		fileName = str(max(fileName))

		try:
			os.chdir(fileName)
			pathSavedModel = os.getcwd()
			print("Path changed:", pathSavedModel)
		except:
			print("Path not found:", sys.exc_info())

		model = keras.models.load_model(pathSavedModel)

		return model
	
	def predict(self):
		model = self.get_model()
		predictions = model.predict(self.test)

		result = [np.argmax(pred) for pred in predictions]

		return result


class Data:

	@staticmethod
	def test_data():
		(train_x, train_y), (test_x, test_y) = keras.datasets.mnist.load_data()

		digit = load_digits()

		digit = digit.images
		digit = digit[0] #test img
		digit = resize(digit, (28, 28))
		digit = digit.reshape(1, 28, 28)
		digit = tf.expand_dims(digit, 3)

		res = Predict(digit)
		res.predict()

if __name__ == '__main__':
	data = Data()
	data.test_data()