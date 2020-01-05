from django.db import models
from .utils import ROOM_TYPES, LOCATION_CHOICES, CAPACITY_ROOMS

from accounts.models import CustomUser


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    location = models.CharField(choices=LOCATION_CHOICES, default='bogota', max_length=50)
    picture = models.CharField(max_length=150)
    likes = models.IntegerField(default=0)
    unlikes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.location.capitalize())

    @property
    def rooms(self):
        return Room.objects.filter(hotel__name=self.name)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, default=1, verbose_name='Hotel', on_delete=models.SET_DEFAULT)
    number_room = models.CharField(max_length=4)
    description = models.TextField(blank=False)
    price = models.IntegerField(default=0)
    capacity = models.CharField(max_length=2, choices=CAPACITY_ROOMS)
    room_type = models.CharField(max_length=30, choices=ROOM_TYPES)
    active = models.BooleanField(default=True)
    picture = models.CharField(max_length=150, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    def __str__(self):
        return '{} - {}  '.format(self.hotel.name, self.number_room)


class Reservation(models.Model):
    date_of_enter = models.DateField(verbose_name='Fecha de Entrada')
    date_of_exit = models.DateField(verbose_name='Fecha de Salida')
    reserved_room = models.ForeignKey(Room, default=1, verbose_name='Room', on_delete=models.SET_DEFAULT)
    user = models.ForeignKey(CustomUser, default=1, verbose_name='User', on_delete=models.SET_DEFAULT)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
