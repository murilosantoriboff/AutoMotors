from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Pedidos
from django.shortcuts import get_object_or_404

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
    pedido = Pedidos.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'editar_pedido.html', {'pedido':pedido})

def excluir_pedido(request, id):
    pedido = get_object_or_404(Pedidos, pk=id)
    pedido.delete()
    return redirect('/automotors/home/')

def gerar_PDF(request, id):
    pass