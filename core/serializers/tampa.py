from rest_framework import serializers
from core.models import Tampa

class TampaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tampa
        fields = '__all__'