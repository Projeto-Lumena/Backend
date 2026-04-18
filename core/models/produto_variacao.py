from django.db import models

from .produto import Produto


class ProdutoVariacao(models.Model):
    TAMANHOS = [
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='variacoes')

    tamanho = models.CharField(max_length=1, choices=TAMANHOS)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.produto.nome} - {self.tamanho}'

    class Meta:
        verbose_name = 'Produto Variação'
        verbose_name_plural = 'Produto Variações'
