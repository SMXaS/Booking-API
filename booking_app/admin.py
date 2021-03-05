"""
This file contains all the admin panel functions
Admin panel can be modified as programmer wants
"""

# Getting access to the admin panel
from django.contrib import admin

# Importing Room database model
from .models import Room

# Registering the Database in the Admin Panel
admin.site.register(Room)
