from django.urls import path

from .views import ListAllBookings, DetailBooking

urlpatterns = [
    path('<int:pk>/', DetailBooking.as_view()),
    path('', ListAllBookings.as_view()),
]