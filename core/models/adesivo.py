from django.db import models

from .tipo import TipoProduto


class Adesivo(models.Model):
    tipo = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    nome_adesivo = models.CharField(max_length=50)
