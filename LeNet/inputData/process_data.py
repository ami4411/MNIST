import tensorflow as tf

class Data:
	"""To capture data and then process the data for a model."""

	def __init__(self, data):
		self.data = data

	def process_data(self):
		"""Data preparation: Transform data, cleaning and organize it for modelling or prediction."""
		self.data = tf.expand_dims(self.data, 3)

		return self.data

	@classmethod
	def normalize_data(cls, test):
		data = test / 255.0

		return cls(data)

	@staticmethod
	def mean_data(x):
		return x.mean()

	@classmethod
	def center_data(cls, test):
		data = test - Data.mean_data(test)

		return cls(data)

	@staticmethod
	def std_data(x):
		return x.std()

	@classmethod
	def standardize_data(cls, test):
		data = (test - Data.mean_data(test)) / Data.std_data(test)

		return cls(data)