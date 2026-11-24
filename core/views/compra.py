from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Compra
from core.serializers import CompraCreateUpdateSerializer, CompraSerializer


class CompraViewSet(ModelViewSet):
    serializer_class = CompraSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Compra.objects
            .filter(usuario=self.request.user)
            .prefetch_related('itens__produto', 'itens__variacao')
            .order_by('-id')
        )

    def get_serializer_class(self):
        if self.action in {'create', 'update', 'partial_update'}:
            return CompraCreateUpdateSerializer

        return CompraSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user, status=Compra.StatusCompra.CARRINHO)

    def perform_update(self, serializer):
        compra = self.get_object()

        if compra.status != Compra.StatusCompra.CARRINHO:
            raise ValidationError('Somente compras que estão na sacola podem ser alteradas.')

        serializer.save()

    @action(detail=True, methods=['post'])
    def finalizar(self, request, pk=None):
        compra = self.get_object()

        if compra.status != Compra.StatusCompra.CARRINHO:
            raise ValidationError('Somente compras que estão na sacola podem ser finalizadas.')

        if not compra.itens.exists():
            raise ValidationError('Não é possível finalizar uma compra sem itens.')

        compra.status = Compra.StatusCompra.FINALIZADO
        compra.save(update_fields=['status'])

        serializer = CompraSerializer(compra)
        return Response(serializer.data, status=status.HTTP_200_OK)
