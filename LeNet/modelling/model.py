import tensorflow as tf
from tensorflow import keras

import numpy as np
import datetime

import os
import sys
import logging as log


class LeNet:
	log.basicConfig(level=log.ERROR, filename="modelling.log", filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	def __init__(data, iterable=(), **datasets): 
		data.__dict__.update(iterable, **datasets)

	def save_result(self, model):
		now = datetime.datetime.now()
		time = now.strftime("%Y%m%d%H%M%S")

		path = os.getcwd() #Main Folder
		dirResult = os.path.join(path+"/saved", time)

		if not os.path.isdir(dirResult):
			os.mkdir(dirResult)

		nameModel = "LeNet"

		try:
			model.save(dirResult)
			print("Model is saved")
		except Exception as e:
			log.error(f"{nameModel} models are not saved!", exc_info=True)

		 # procedural func

	def train_model(self):
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
			print("Modelling: finish")
		except:

		# return() # procedural func

class AlexNet:
	pass

class GoogLeNet:
	pass

class VGGNet:
	pass

class ResNet:
	pass

class DenseNet:
	pass

def main():
	(train_x, train_y), (test_x, test_y) = keras.datasets.mnist.load_data()
	train_x = train_x / 255.0 
	test_x = test_x / 255.0 
	train_x = tf.expand_dims(train_x, 3)
	test_x = tf.expand_dims(test_x, 3)
	val_x = train_x[:5000]
	val_y = train_y[:5000]
	
	model = LeNet(train_x=train_x, test_x=test_x, train_y=train_y, test_y=test_y, val_x=val_x, val_y=val_y)
	model.train_model()

	return None


if __name__ == '__main__':
	main()