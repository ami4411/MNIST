import tensorflow as tf
from tensorflow import keras

import numpy as np
import h5py

import os
import sys
import datetime

class Predict:

	def __init__(self, test, dt=None):
		self.test = test
		self.dt = dt

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

	@staticmethod
	def save_pred(result):

		now = datetime.datetime.now()
		time = now.strftime("%H%M%S")
		date = now.strftime("%Y%m%d")

		os.chdir("../../")
		path = os.getcwd()

		dir_file = os.path.join(path+"/output", date)
		if not os.path.isdir(dir_file):
			os.mkdir(dir_file)
		
		os.chdir(dir_file)

		with h5py.File(time+'.h5', 'w') as file:
			file.create_dataset("Result", data=result)
	
	def predict(self):
		model = self.get_model()
		predictions = model.predict(self.test)

		result = [np.argmax(pred) for pred in predictions]
		self.save_pred(result)

		if isinstance(self.dt, np.ndarray):
			_, acc = model.evaluate(self.test, self.dt, verbose=0)
			print('Accuracy> %.3f' % (acc * 100.0))

		return result


