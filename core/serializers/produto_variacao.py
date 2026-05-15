from rest_framework.serializers import ModelSerializer

from core.models import ProdutoVariacao


class ProdutoVariacaoSerializer(ModelSerializer):
    class Meta:
        model = ProdutoVariacao
        fields = '__all__'
