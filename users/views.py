from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirme_senha')
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            return redirect('/users/cadastro/?message=ERROR')
        if senha != confirmar_senha:
            return redirect('/users/cadastro/?message=ERROR')
        try:
            user = User.objects.get(email=email)
            if user:
                return redirect('/users/cadastro/?message=EMAIL_ERROR')
        except:
            user = User.objects.create_user(nome, email, senha)
            user.save()
            return redirect('/users/login/')



def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('password')

        user = authenticate(username=nome, password=senha)

        if user is not None:
            return redirect('/automotors/home/')
        return redirect('/users/login/?message=ERROR')