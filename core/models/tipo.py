from django.db import models


class TipoProduto(models.Model):
    nome_tipo = models.CharField(max_length=50)
