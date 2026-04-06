from django.db import models

from .pedido import Pedido

class Pagamento(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    data_pagamento = models.DateField()
    metodo = models.CharField(max_length=50)
