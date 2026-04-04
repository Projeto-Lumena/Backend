from rest_framework import serializers
from core.models import tampa

class TampaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tampa
        fields = '__all__'