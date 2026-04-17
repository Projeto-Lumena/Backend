from rest_framework.viewsets import ModelViewSet

from core.models import Embalagem
from core.serializers import EmbalagemSerializer


class EmbalagemViewSet(ModelViewSet):
    queryset = Embalagem.objects.all()
    serializer_class = EmbalagemSerializer
