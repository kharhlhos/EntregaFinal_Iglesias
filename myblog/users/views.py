# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})
# Create your views here.

def login_view(request):
    next_url = request.GET.get('next', '/')  # Obtiene la URL a la que redirigir después del inicio de sesión
    if request.method == 'POST':
        # Lógica de autenticación aquí
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_url)  # Redirige a la URL especificada en 'next'
    return render(request, 'users/login.html')
