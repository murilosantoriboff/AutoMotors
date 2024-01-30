from django.contrib import admin
from . import models

admin.site.register(models.Clientes)
admin.site.register(models.Produtos)
admin.site.register(models.Pedidos)
admin.site.register(models.Feedback)