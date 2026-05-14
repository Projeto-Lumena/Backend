from rest_framework.serializers import ModelSerializer

from core.models import Produto


class ProdutoListSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id', 'nome')


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class ProdutoRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
        depth = 1
