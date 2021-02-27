from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # This points to the booking app and .urls.py file
    path('api/', include('booking_app.urls')), 
]