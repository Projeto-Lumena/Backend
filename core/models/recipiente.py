from django.db import models
from .tipo import TipoProduto

class Recipiente(models.Model):
    tipo = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    tamanho = models.CharField(max_length=10)