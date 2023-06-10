from django.urls import path
from .views import login, crear

urlpatterns = [
    path('login/', login, name="login"),
    path('crear/', crear, name="crear"),
]