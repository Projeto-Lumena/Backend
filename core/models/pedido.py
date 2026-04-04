from django.db import models

from .user import User

class Pedido(models.Model):
    usuario = models.ForeignKey( User, on_delete=models.PROTECT)
    data_pedido = models.DateField()
    status = models.CharField(max_length=20)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_entrega = models.DateField(null=True, blank=True)