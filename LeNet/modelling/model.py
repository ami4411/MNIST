import tensorflow as tf
from tensorflow import keras

import numpy as np
import datetime

import sys
import os
from logger.log import Logger

from inputData import data
from inputData.process_data import *

class LeNet:
	def __init__(data, iterable=(), **datasets): 
		data.__dict__.update(iterable, **datasets)

	def save_result(self, model):
		log.info("Saving...")
		now = datetime.datetime.now()
		time = now.strftime("%Y%m%d%H%M%S")

		path = os.getcwd() #Main Folder
		dirResult = os.path.join(path+"/saved", time)

		if not os.path.isdir(dirResult):
			os.mkdir(dirResult)

		nameModel = "LeNet"

		try:
			model.save(dirResult)
			log.info("Model is saved")
		except Exception as e:
			log.error(f"{nameModel} models are not saved!", exc_info=True)

		 # procedural func

	def train_model(self):
		log.info("Training...")
		lenetRelu = keras.models.Sequential([
		    keras.layers.Conv2D(6, kernel_size=5, strides=1,  activation='relu', input_shape=self.train_x[0].shape, padding='same'), 
		    keras.layers.AveragePooling2D(), 
		    keras.layers.Conv2D(16, kernel_size=5, strides=1, activation='relu', padding='same'), 
		    keras.layers.AveragePooling2D(), 
		    keras.layers.Flatten(), 
		    keras.layers.Dense(120, activation='relu'), 
		    keras.layers.Dense(84, activation='relu'), 
		    keras.layers.Dense(10, activation='softmax') 
		])
		lenetRelu.compile(optimizer='adam', loss=keras.losses.sparse_categorical_crossentropy, metrics=['accuracy'])
		lenetRelu.fit(self.train_x, self.train_y, epochs=5, validation_data=(self.val_x, self.val_y))

		try:
			self.save_result(lenetRelu)
			log.info("Modelling: finish")
		except:
			pass

def main():
	train_x, train_y, test_x, test_y = data.get_data(2)

	def norm_process():		
		nonlocal train_x, test_x

		result = list()
		for val in [train_x, test_x]:
			result.append(Data.process_data(Data.normalize_data(val)))

		train_x, test_x = result

	norm_process()
	val_x, val_y  = train_x[:5000], train_y[:5000]

	model = LeNet(train_x=train_x, test_x=test_x, train_y=train_y, test_y=test_y, val_x=val_x, val_y=val_y)
	model.train_model()

	return None


if __name__ == '__main__':
	run = "dev"
	log = Logger(run).log()
	main()