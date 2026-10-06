from django.db import transaction
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Compra
from core.serializers import (
    CompraCreateUpdateSerializer,
    CompraListSerializer,
    CompraSerializer,
)


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.order_by('-id')
    serializer_class = CompraSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self):
        if self.action == 'list':
            return CompraListSerializer

        if self.action in {'create', 'update'}:
            return CompraCreateUpdateSerializer

        return CompraSerializer

    def get_queryset(self):
        usuario = self.request.user

        if usuario.is_superuser:
            return Compra.objects.all().order_by('-id')

        if usuario.groups.filter(name='administradores').exists():
            return Compra.objects.all().order_by('-id')

        return Compra.objects.filter(usuario=usuario).order_by('-id')

    @action(detail=True, methods=['post'])
    @transaction.atomic
    def finalizar(self, request, pk=None):
        compra = self.get_object()

        if compra.status != Compra.StatusCompra.CARRINHO:
            return Response(
                {'status': 'A compra não está no carrinho'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        compra.status = Compra.StatusCompra.FINALIZADO
        compra.save()

        return Response(
            {'status': 'Compra finalizada'},
            status=status.HTTP_200_OK,
        )
