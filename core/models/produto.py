from django.db import models

from uploader.models import Image

from .categoria import Categoria


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ForeignKey(
        Image,
        related_name='+',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    ativo = models.BooleanField(default=True)

    categorias = models.ManyToManyField(Categoria, related_name='produtos')

    def __str__(self):
        return self.nome
