from django.db import models

from .tipo_produto import TipoProduto

class Tampa(models.Model):
    tipo = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    tamanho = models.CharField(max_length=10)