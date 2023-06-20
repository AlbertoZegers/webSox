from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm, CreateUserForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('visualizacion')
    else:
        form = LoginForm()
        
    return render(request, 'usuario/pagLogin.html', {'form': form})


def crear(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visualizacion')
    else:
        form = CreateUserForm()
        
    return render(request, 'usuario/pagCrear.html', {'form': form})