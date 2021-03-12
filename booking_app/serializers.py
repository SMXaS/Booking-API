"""
Serializers file which allow to display data mostly in JSON file
"""
from rest_framework import serializers
from .models import Room

# Creating Booking Serializer which display all fields
class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('__all__')
