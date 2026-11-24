from django.db.models import Max, Min
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from core.models import Produto
from core.serializers import (
    ProdutoListSerializer,
    ProdutoRetrieveSerializer,
    ProdutoSerializer,
)


class ProdutoViewSet(ModelViewSet):
    serializer_class = ProdutoSerializer

    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = ['nome', 'categorias__nome']

    ordering_fields = [
        'nome',
        'preco_min',
        'preco_max',
    ]

    ordering = ['nome']

    def get_queryset(self):
        return Produto.objects.annotate(
            preco_min=Min('variacoes__preco'),
            preco_max=Max('variacoes__preco'),
        )

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)

        # Filtragem por uma ou mais categorias.
        categorias = self.request.query_params.get('categorias')

        if categorias:
            try:
                ids = [int(categoria) for categoria in categorias.split(',') if categoria.strip()]
            except ValueError:
                return queryset.none()

            if ids:
                queryset = queryset.filter(categorias__id__in=ids)

        return queryset.distinct()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProdutoListSerializer
        elif self.action == 'retrieve':
            return ProdutoRetrieveSerializer

        return ProdutoSerializer
