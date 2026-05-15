from rest_framework.serializers import ModelSerializer

from core.models import Aroma


class AromaSerializer(ModelSerializer):
    class Meta:
        model = Aroma
        fields = '__all__'
