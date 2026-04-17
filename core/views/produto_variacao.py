from rest_framework.viewsets import ModelViewSet

from core.models import ProdutoVariacao
from core.serializers import ProdutoVariacaoSerializer


class ProdutoVariacaoViewSet(ModelViewSet):
    queryset = ProdutoVariacao.objects.all()
    serializer_class = ProdutoVariacaoSerializer
