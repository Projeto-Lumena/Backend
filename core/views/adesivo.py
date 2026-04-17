from rest_framework.viewsets import ModelViewSet

from core.models import Adesivo
from core.serializers import AdesivoSerializer


class AdesivoViewSet(ModelViewSet):
    queryset = Adesivo.objects.all()
    serializer_class = AdesivoSerializer
