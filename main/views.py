from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Usar o Login Required
# Fazer a função de Logout

def logout_sair(request):
    logout(request)
    return redirect('/users/login/')

@login_required
def home(request):
    return render(request, 'home.html')
