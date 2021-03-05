"""
This file contains all modified models
Models represent database
"""

# Importing models database
from django.db import models

# Class Room database model
class Room(models.Model):
    # Declaring the options to pick from
    ROOM_NAMES = (
        ('1', 'Meeting Room 1'),
        ('2', 'Meeting Room 2'),
        ('3', 'Meeting Room 3'),       
    )
    # Declaring all keys that needs be filled for booking
    title = models.CharField(max_length=50)
    room_name = models.CharField(max_length=1, choices =ROOM_NAMES)
    employee_id = models.IntegerField()
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()

    def __str__(self):
        return self.title
    