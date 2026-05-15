from rest_framework.serializers import ModelSerializer

from core.models import Fita


class FitaSerializer(ModelSerializer):
    class Meta:
        model = Fita
        fields = '__all__'
