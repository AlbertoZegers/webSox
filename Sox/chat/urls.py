from django.urls import path
from .views import home, descripcion

urlpatterns = [
    path('', home, name="home"),
    path('descripcion/', descripcion, name="descripcion"),
]