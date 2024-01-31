from django.shortcuts import render, redirect
from django.contrib.auth import logout

def logout_sair(request):
    logout(request)
    return redirect('/users/login/')

def home(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'home.html')
    else:
        return redirect('/users/login/')
