"""
This is the main file of the API
The file contains [Get, Post, Update, Delete] API Requests
"""
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers
from .models import Room
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

        # TODO Why ROOM model only? What about reservations model? 
        # TODO Create Employees
        # TODO Think about ID of User that registering
        # TODO Think about Room numbers [1,9] available now, 10 ... 11 will cause trouble
        # TODO Tests
        