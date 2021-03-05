"""
This file contains routes or entry-point for API endpoints
"""

# Importing the path function for getting routes navigation
from django.urls import path

# From views file importing classes
from .views import ListAllBookings, DetailBooking

urlpatterns = [
    # Displays the specific booking /api/1
    path('<int:pk>/', DetailBooking.as_view()),
    
    # Displays all bookings /api
    path('', ListAllBookings.as_view()),
]
