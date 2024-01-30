from django.db import models

class Clientes(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=500)
    telefone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Produtos(models.Model):
    nome = models.CharField(max_length=200)
    preço = models.FloatField()
    descricao = models.TextField()
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome

class Pedidos(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produtos)
    quantidade = models.IntegerField(default=0)
    data_pedido = models.DateField()
    data_entrega = models.DateField()
    valor_total = models.FloatField()

    def __str__(self):
        return f'Pedido {self.id}'

class Feedback(models.Model):
    choices = (
        ('B', 'Bom'),
        ('R', 'Ruim')
    )
    escolha = models.CharField(max_length=1, choices=choices)
    feedback = models.TextField()

    def __str__(self):
        return f'Feedback {self.id}'