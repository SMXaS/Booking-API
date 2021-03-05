"""
This is the main file of the API
The file contains [Get, Post, Update, Delete] API Requests
"""
# Allows to get common usage patterns
from rest_framework import generics

# Importing status server codes
from rest_framework import status

# Importing API view decorators
from rest_framework.decorators import api_view

# Importing response from the API
from rest_framework.response import Response

# Importing API view
from rest_framework.views import APIView

# Importing models file
from . import models

# Importing serializers file
from . import serializers

# Importing room database model
from .models import Room

# Importing bookings serializer class
from .serializers import BookingsSerializer

# Displays all the Bookings /api
class ListAllBookings(APIView):
    
    def get(self, request):
        # From Room model gets all objects
        articles = models.Room.objects.all()
        serializer = serializers.BookingsSerializer(articles,   
                                                  many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Posting function, displays all made bookings
        serializer=serializers.BookingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                           status=status.HTTP_201_CREATED)
        return Response(serializer.errors, 
                       status=status.HTTP_400_BAD_REQUEST)

# Displays detailed booking /api/1                  
class DetailBooking(APIView):
    
    # Gets all data from the server
    def get(self, request, pk):
        article = models.Room.objects.get(id=pk)
        serializer = serializers.BookingsSerializer(article)
        return Response(serializer.data)
    
    # Updates the data
    def put(self, request, pk):
        article = models.Room.objects.get(id=pk)
        serializer = serializers.BookingsSerializer(article, 
                                                  request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, 
                       status=status.HTTP_400_BAD_REQUEST)

    # Deletes the data
    def delete(self, request, pk):
        article = models.Room.objects.get(id=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        