from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Hotel


class HotelList(ListView):
    model = Hotel
    template_name = 'booking/list-hotel.html'


class HotelDetail(DetailView):
    model = Hotel


class HotelCreate(CreateView):
    model = Hotel
    template_name = 'booking/create-hotel.html'
    success_url = reverse_lazy('list_hotel')
    fields = ['name', 'description', 'location', 'picture']


class HotelUpdate(CreateView):
    model = Hotel
    success_url = reverse_lazy('booking:list')
    fields = ['name', 'description', 'location', 'picture']


class HotelDelete(DeleteView):
    model = Hotel
    success_url = reverse_lazy('booking:list')
