from rest_framework import serializers
from core.models import Adesivo

class AdesivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adesivo
        fields = '__all__'