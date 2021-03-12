"""
This file contains all the admin panel functions
Admin panel can be modified as programmer wants
"""
from django.contrib import admin
from .models import Room

# Registering the Database in the Admin Panel
admin.site.register(Room)
