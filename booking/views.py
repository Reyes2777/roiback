from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Hotel, Room


class HotelList(ListView):
    model = Hotel
    template_name = 'booking/home.html'


class HotelDetail(DetailView):
    model = Hotel
    template_name = 'booking/detail-hotel.html'


class HotelCreate(CreateView):
    model = Hotel
    template_name = 'booking/form-hotel.html'
    success_url = reverse_lazy('home')
    fields = ['name', 'description', 'location', 'picture']


class HotelUpdate(UpdateView):
    model = Hotel
    template_name = 'booking/form-hotel.html'
    success_url = reverse_lazy('home')
    fields = ['name', 'description', 'location', 'picture']


class HotelDelete(DeleteView):
    model = Hotel
    template_name = 'booking/confirm-delete.html'
    success_url = reverse_lazy('home')


class RoomCreate(CreateView):
    model = Room
    template_name = 'booking/form-room.html'
    success_url = reverse_lazy('home ')
    fields = ['hotel', 'number_room', 'description', 'capacity', 'room_type']


class RoomUpdate(UpdateView):
    model = Room
    template_name = 'booking/form-room.html'
    success_url = reverse_lazy('home')
    fields = ['hotel', 'number_room', 'description', 'capacity', 'room_type']


class RoomDelete(DeleteView):
    model = Room
    template_name = 'booking/confirm-delete.html'
    success_url = reverse_lazy('list_hotel')
