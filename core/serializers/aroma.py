from rest_framework import serializers

from core.models import Aroma


class AromaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aroma
        fields = '__all__'
