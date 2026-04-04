from rest_framework.viewsets import ModelViewSet

from core.models import tampa
from core.serializers import TampaSerializer

class TampaViewSet(ModelViewSet):   
    queryset = tampa.objects.all()
    serializer_class = TampaSerializer