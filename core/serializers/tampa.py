from rest_framework.serializers import ModelSerializer

from core.models import Tampa


class TampaSerializer(ModelSerializer):
    class Meta:
        model = Tampa
        fields = '__all__'
