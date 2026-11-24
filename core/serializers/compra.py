from django.db import transaction
from rest_framework import serializers
from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    SerializerMethodField,
)

from core.models import Compra, ItensCompra


class ItensCompraCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('produto', 'variacao', 'quantidade')

    def validate(self, data):
        produto = data.get('produto')
        variacao = data.get('variacao')

        if (
            produto
            and variacao
            and variacao.produto_id != produto.id
        ):
            raise serializers.ValidationError(
                'A variação informada não pertence ao produto selecionado.'
            )

        if data.get('quantidade', 1) <= 0:
            raise serializers.ValidationError(
                'A quantidade deve ser maior que zero.'
            )

        return data


class CompraCreateUpdateSerializer(ModelSerializer):
    itens = ItensCompraCreateUpdateSerializer(many=True)

    class Meta:
        model = Compra
        fields = ('id', 'itens')

    @transaction.atomic
    def create(self, validated_data):
        itens = validated_data.pop('itens')

        compra = Compra.objects.create(**validated_data)

        for item in itens:
            ItensCompra.objects.create(compra=compra, **item)

        return compra

    @transaction.atomic
    def update(self, instance, validated_data):
        itens = validated_data.pop('itens', None)

        if itens is not None:
            instance.itens.all().delete()

            for item in itens:
                ItensCompra.objects.create(compra=instance, **item)

        return instance


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.variacao.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ('produto', 'variacao', 'quantidade', 'total')
        depth = 1


class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email', read_only=True)
    status = CharField(source='get_status_display', read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'status', 'total', 'itens')
