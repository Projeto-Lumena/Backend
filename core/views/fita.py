from rest_framework.viewsets import ModelViewSet

from core.models import Fita
from core.serializers import FitaSerializer


class FitaViewSet(ModelViewSet):
    queryset = Fita.objects.all()
    serializer_class = FitaSerializer
