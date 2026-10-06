from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.models import Compra
from core.serializers import CompraCreateUpdateSerializer, CompraSerializer


class CompraViewSet(ModelViewSet):
    serializer_class = CompraSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Compra.objects.filter(
            usuario=self.request.user
        ).prefetch_related(
            'itens__produto',
            'itens__variacao'
        ).order_by('-id')

    def get_serializer_class(self):
        if self.action in {'create', 'update', 'partial_update'}:
            return CompraCreateUpdateSerializer

        return CompraSerializer

    def perform_create(self, serializer):
        serializer.save(
            usuario=self.request.user,
            status=Compra.StatusCompra.FINALIZADO
        )