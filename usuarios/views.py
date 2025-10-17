from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

# Create your views here.
def usuario_login(request):
    if request.method == "POST":
        nome_usuario = request.POST.get('username')
        senha = request.POST.get('password')

        usuario = authenticate(username = nome_usuario, password = senha)

        if usuario is not None:
            login(request, usuario)
            return redirect(reverse('home'))
        
        return HttpResponse('Usuario não existe')

    return render(request, 'login.html')

def cadastro_usuario(request):
    if request.method == "POST":
        nome_usuario = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        senha2 = request.POST.get('password2')

        usuario = User.objects.create_user(
            username = nome_usuario,
            email = email,
            password = senha
        )

        return redirect(reverse('login'))

    return render(request, 'login.html')

def logout_usuario(request):
    logout(request)
    return redirect(reverse('home'))