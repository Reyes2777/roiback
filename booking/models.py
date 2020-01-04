from django.db import models
from .utils import ROOM_TYPES, LOCATION_CHOICES, CAPACITY_ROOMS

from accounts.models import CustomUser


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    location = models.CharField(choices=LOCATION_CHOICES, default='bogota', max_length=50)
    picture = models.CharField(max_length=120)
    likes = models.IntegerField(default=0)
    unlikes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{} '.format(self.name)

    @property
    def rooms(self):
        return Room.objects.filter(hotel__name=self.name)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, default=1, verbose_name='Hotel', on_delete=models.SET_DEFAULT)
    number_room = models.CharField(max_length=4)
    description = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    capacity = models.CharField(max_length=2, choices=CAPACITY_ROOMS)
    room_type = models.CharField(max_length=30, choices=ROOM_TYPES)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')


class Reservation(models.Model):
    date_of_enter = models.DateField(verbose_name='Fecha de Entrada')
    date_of_exit = models.DateField(verbose_name='Fecha de Salida')
    reserved_room = models.ForeignKey(Room, default=1, verbose_name='Room', on_delete=models.SET_DEFAULT)
    user = models.ForeignKey(CustomUser, default=1, verbose_name='User', on_delete=models.SET_DEFAULT)
