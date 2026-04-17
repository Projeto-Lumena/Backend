from django.db import models

from .categoria import Categoria


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='produtos/')
    ativo = models.BooleanField(default=True)

    categorias = models.ManyToManyField(Categoria, related_name='produtos')

    def __str__(self):
        return self.nome
