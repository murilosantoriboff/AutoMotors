from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Pedidos

def logout_sair(request):
    logout(request)
    return redirect('/users/login/')

def home(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            pedidos = Pedidos.objects.all()
            return render(request, 'home.html', {'pedidos':pedidos})
    else:
        return redirect('/users/login/')

def editar_pedido(request, id):
    pass

def gerar_PDF(request, id):
    pass