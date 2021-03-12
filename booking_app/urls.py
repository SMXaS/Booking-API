"""
This file contains routes or entry-point for API endpoints
"""
from django.urls import path
from .views import ListAllBookings, DetailBooking

urlpatterns = [
    # Displays the specific booking /api/1
    path('<int:pk>/', DetailBooking.as_view()),
    
    # Displays all bookings /api
    path('', ListAllBookings.as_view()),
]
