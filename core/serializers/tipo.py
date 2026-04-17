from rest_framework import serializers

from core.models import TipoProduto


class TipoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProduto
        fields = '__all__'
