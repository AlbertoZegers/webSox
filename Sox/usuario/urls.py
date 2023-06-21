from django.urls import path
from usuario import views

urlpatterns = [
    path('crear/', views.crear, name="crear"),
]