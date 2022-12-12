from rest_framework import serializers

from .models import Snacks
class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model= Snacks
        # fields=['id','name', 'owner', 'description']
        fields='__all__'