from django.db import models

from .produto import Produto
from .user import User


class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField(max_length=500, blank=True, null=True)
    data_avaliacao = models.DateField()

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
