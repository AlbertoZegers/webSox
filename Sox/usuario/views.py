from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm, CreateUserForm

def crear(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
        
    return render(request, 'usuario/pagCrear.html', {'form': form})