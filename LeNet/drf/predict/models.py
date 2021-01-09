from django.db import models
import h5py
import django.utils.timezone as timezone

class Predict(models.Model):
	result = models.IntegerField()
	time_insert = models.DateTimeField(default=timezone.now(), editable=False)

	def __str__(self):
		return str(self.result)
