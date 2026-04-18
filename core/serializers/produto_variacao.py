from rest_framework import serializers

from core.models import ProdutoVariacao


class ProdutoVariacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoVariacao
        fields = '__all__'
