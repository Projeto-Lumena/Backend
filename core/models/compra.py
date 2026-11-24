from django.db import models
from django.db.models import Q

from .produto import Produto
from .produto_variacao import ProdutoVariacao
from .user import User


class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        FINALIZADO = 2, 'Finalizado'
        PAGO = 3, 'Pago'
        ENTREGUE = 4, 'Entregue'

    class TipoPagamento(models.IntegerChoices):
        PIX = 1, 'PIX'
        DINHEIRO = 2, 'Dinheiro'

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='compras')

    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)

    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    tipo_pagamento = models.IntegerField(choices=TipoPagamento.choices, default=TipoPagamento.PIX)

    @property
    def total(self):
        return sum(item.preco * item.quantidade for item in self.itens.all())

    def __str__(self):
        return f'Pedido #{self.id}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['usuario'], condition=Q(status=1), name='unique_carrinho_por_usuario')
        ]


class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens')

    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='+')

    variacao = models.ForeignKey(ProdutoVariacao, on_delete=models.PROTECT, related_name='+')

    quantidade = models.IntegerField(default=1)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.produto.nome} - Pedido #{self.compra.id}'

    class Meta:
        verbose_name = 'Item da Compra'
        verbose_name_plural = 'Itens da Compra'
