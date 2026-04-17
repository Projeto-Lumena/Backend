from rest_framework.viewsets import ModelViewSet

from core.models import Tampa
from core.serializers import TampaSerializer


class TampaViewSet(ModelViewSet):
    queryset = Tampa.objects.all()
    serializer_class = TampaSerializer
