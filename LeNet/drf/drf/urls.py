from django.contrib import admin
from django.urls import include, path
from predict.views import PredictViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('predict', PredictViewSet, basename='Predict')

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api-auth/', include('rest_framework.urls')),
	path('', include(router.urls)),
]

