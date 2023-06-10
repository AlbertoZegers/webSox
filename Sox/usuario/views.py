from django.shortcuts import render

# Create your views here.
def crear(request):
    return render(request, 'usuario/pagCrear.html')
def login(request):
    return render(request, 'usuario/pagLogin.html')