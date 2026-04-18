from django.db import models


class Pavio(models.Model):
    quantidade = models.IntegerField()
    tamanho = models.CharField(max_length=10)
