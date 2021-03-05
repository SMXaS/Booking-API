"""
Serializers file which allow to display data mostly in JSON file
"""
# Importing serializers to translate data
from rest_framework import serializers

# Importing Room database model 
from .models import Room

# Creating Booking Serializer which display all fields
class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('__all__')
