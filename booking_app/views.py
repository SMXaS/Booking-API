from rest_framework import generics


from .models import Room
from .serializers import BookingsSerializer


class ListAllBookings(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = BookingsSerializer

class DetailBooking(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = BookingsSerializer
