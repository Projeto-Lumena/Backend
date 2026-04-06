from rest_framework.viewsets import ModelViewSet

from core.models import TipoProduto
from core.serializers import TipoProdutoSerializer


class TipoProdutoViewSet(ModelViewSet):
    queryset = TipoProduto.objects.all()
    serializer_class = TipoProdutoSerializer