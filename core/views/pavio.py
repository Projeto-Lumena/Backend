from rest_framework.viewsets import ModelViewSet

from core.models import Pavio
from core.serializers import PavioSerializer


class PavioViewSet(ModelViewSet):
    queryset = Pavio.objects.all()
    serializer_class = PavioSerializer
