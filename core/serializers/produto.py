from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Produto
from uploader.models import Image
from uploader.serializers import ImageSerializer


class ProdutoListSerializer(ModelSerializer):
    imagem = ImageSerializer()

    class Meta:
        model = Produto
        fields = ('id', 'nome', 'descricao', 'imagem', 'categorias')


class ProdutoRetrieveSerializer(ModelSerializer):
    imagem = ImageSerializer(required=False)

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'imagem', 'ativo', 'categorias', 'variacoes', 'avaliacao_set']
        depth = 1


class ProdutoSerializer(ModelSerializer):
    imagem_attachment_key = SlugRelatedField(
        source='imagem',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True,
    )
    imagem = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Produto
        fields = '__all__'
