from rest_framework import generics

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers
from .models import Room
from .serializers import BookingsSerializer


class ListAllBookings(APIView):
    
    def get(self, request):
        articles = models.Room.objects.all()
        serializer = serializers.BookingsSerializer(articles,   
                                                  many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=serializers.BookingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                           status=status.HTTP_201_CREATED)
        return Response(serializer.errors, 
                       status=status.HTTP_400_BAD_REQUEST)
class DetailBooking(APIView):
    
    def get(self, request, pk):
        article = models.Room.objects.get(id=pk)
        serializer = serializers.BookingsSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk):
        article = models.Room.objects.get(id=pk)
        serializer = serializers.BookingsSerializer(article, 
                                                  request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        article = models.Room.objects.get(id=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)