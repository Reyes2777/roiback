from django.db import models
from .utils.locations_choices import location_choices


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    location = models.CharField(choices=location_choices, default='Bogota', max_length=50)
    picture = models.CharField(max_length=120)
    likes = models.IntegerField(default=0)
    unlikes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, default=1, verbose_name='Hotel', on_delete=models.SET_DEFAULT)
    number_room = models.CharField(max_length=4)
    description = models.CharField(max_length=100)
    capacity = models.CharField(max_length=2)
    room_type = models.CharField(max_length=30)
