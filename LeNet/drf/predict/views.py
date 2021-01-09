from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import PredictSerializer
from .models import Predict

class PredictViewSet(ReadOnlyModelViewSet):

	serializer_class = PredictSerializer
	queryset = Predict.objects.all()
