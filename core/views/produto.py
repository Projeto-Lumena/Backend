from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from core.models import Produto
from core.serializers import ProdutoListSerializer, ProdutoRetrieveSerializer, ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['categorias__nome']
    search_fields = ['nome', 'categorias__nome']
    ordering_fields = ['nome']
    ordering = ['nome']

    def get_serializer_class(self):
        if self.action == 'list':
            return ProdutoListSerializer
        elif self.action == 'retrieve':
            return ProdutoRetrieveSerializer
        return ProdutoSerializer
