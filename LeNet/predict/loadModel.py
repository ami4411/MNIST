import tensorflow as tf
from tensorflow import keras

import numpy as np

import os

(train_x, train_y), (test_x, test_y) = keras.datasets.mnist.load_data()
test_x = test_x / 255.0

test_x = tf.expand_dims(test_x, 3)
pathResult = os.chdir("result")

fileName = [int(x) for x in os.listdir()]
fileName = str(max(fileName))

os.chdir(fileName)
pathSavedModel = os.getcwd()

model = keras.models.load_model(pathSavedModel)

predictions = model.predict(test_x[:10])
result = [np.argmax(a) for a in predictions]
print(result)