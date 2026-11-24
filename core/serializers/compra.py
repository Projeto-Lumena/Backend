from django.db import transaction
from rest_framework import serializers
from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,
    DateTimeField,
    HiddenField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)

from core.models import Compra, ItensCompra


class ItensCompraCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('produto', 'variacao', 'quantidade', 'preco')
        read_only_fields = ('preco',)

    def validate_quantidade(self, quantidade):
        if quantidade <= 0:
            raise ValidationError('A quantidade deve ser maior do que zero.')
        return quantidade

    def validate(self, data):
        produto = data.get('produto')
        variacao = data.get('variacao')

        if produto and variacao and variacao.produto_id != produto.id:
            raise serializers.ValidationError('A variação informada não pertence ao produto selecionado.')

        if data.get('quantidade', 1) <= 0:
            raise serializers.ValidationError('A quantidade deve ser maior que zero.')

        return data


class CompraCreateUpdateSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())
    itens = ItensCompraCreateUpdateSerializer(many=True)

    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'tipo_pagamento', 'itens')

    @transaction.atomic
    def create(self, validated_data):
        itens = validated_data.pop('itens')
        usuario = validated_data['usuario']

        compra, criada = Compra.objects.get_or_create(
            usuario=usuario,
            status=Compra.StatusCompra.CARRINHO,
            defaults=validated_data,
        )

        if not criada and 'tipo_pagamento' in validated_data:
            compra.tipo_pagamento = validated_data['tipo_pagamento']
            compra.save()

        for item in itens:
            item_existente = compra.itens.filter(
                produto=item['produto'],
                variacao=item['variacao'],
            ).first()

            if item_existente:
                item_existente.quantidade += item['quantidade']
                item_existente.preco = item['variacao'].preco
                item_existente.save()
            else:
                item['preco'] = item['variacao'].preco
                ItensCompra.objects.create(compra=compra, **item)

        return compra

    @transaction.atomic
    def update(self, instance, validated_data):
        itens = validated_data.pop('itens', None)

        if itens is not None:
            instance.itens.all().delete()

            for item in itens:
                item['preco'] = item['variacao'].preco
                ItensCompra.objects.create(compra=instance, **item)

        return instance


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.quantidade * instance.preco

    class Meta:
        model = ItensCompra
        fields = ('produto', 'variacao', 'quantidade', 'preco', 'total')
        depth = 1


class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email', read_only=True)
    status = CharField(source='get_status_display', read_only=True)
    data_criacao = DateTimeField(read_only=True)
    data_atualizacao = DateTimeField(read_only=True)
    tipo_pagamento = CharField(source='get_tipo_pagamento_display', read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'status', 'total', 'data_criacao', 'data_atualizacao', 'tipo_pagamento', 'itens')


class ItensCompraListSerializer(ModelSerializer):
    produto_id = serializers.IntegerField(source='produto.id', read_only=True)
    produto = CharField(source='produto.nome', read_only=True)

    variacao_id = serializers.IntegerField(source='variacao.id', read_only=True)
    variacao = CharField(source='variacao.tamanho', read_only=True)

    imagem = serializers.SerializerMethodField()

    def get_imagem(self, instance):
        imagem = instance.produto.imagem

        if imagem:
            return {'url': imagem.url}

        return None

    class Meta:
        model = ItensCompra
        fields = (
            'produto_id',
            'produto',
            'variacao_id',
            'variacao',
            'quantidade',
            'preco',
            'imagem',
        )


class CompraListSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email', read_only=True)
    status = CharField(source='get_status_display', read_only=True)
    itens = ItensCompraListSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'status', 'total', 'itens')
