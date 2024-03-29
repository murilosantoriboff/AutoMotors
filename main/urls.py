from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('logout/', views.logout_sair, name='logout_sair'),
    path('editar_pedido/<int:id>', views.editar_pedido, name='editar_pedido'),
    path('gerar_pdf/<int:id>', views.gerar_PDF, name='gerar_pdf'),
    path('excluir_pedido/<int:id>', views.excluir_pedido, name='excluir_pedido'),
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente')
]