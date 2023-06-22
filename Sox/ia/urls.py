from django.urls import path
from .views import visualizacion, feedback, modificar, eliminar 

urlpatterns = [
    path('visualizacion/', visualizacion, name="visualizacion"),
    path('feedback/', feedback, name="feedback"),
    path('modificar/<id>', modificar, name="modificar"),
    path('eliminar/<id>', eliminar, name="eliminar")
]