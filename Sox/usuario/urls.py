from django.urls import path
from usuario import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('crear/', views.crear, name="crear"),
]