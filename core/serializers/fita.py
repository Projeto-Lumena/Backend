from rest_framework import serializers

from core.models import Fita


class FitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fita
        fields = '__all__'
