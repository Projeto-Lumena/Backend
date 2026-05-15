from rest_framework.serializers import ModelSerializer

from core.models import TipoProduto


class TipoProdutoSerializer(ModelSerializer):
    class Meta:
        model = TipoProduto
        fields = '__all__'
