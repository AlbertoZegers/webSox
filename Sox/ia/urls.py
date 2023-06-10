from django.urls import path
from .views import visualizacion, feedback 

urlpatterns = [
    path('visualizacion/', visualizacion, name="visualizacion"),
    path('feedback/', feedback, name="feedback"),
]