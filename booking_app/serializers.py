from rest_framework import serializers
from .models import Room

class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('__all__')
