from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Hotel, Room


def filter_view(request):
    room = Room.objects.all()
    location_room_query = request.GET.get('location_room').lower()
    capacity_room_query = request.GET.get('capacity_room')
    date_in_query = request.GET.get('date_in')
    date_out_query = request.GET.get('date_out')
    print(location_room_query)
    query_set = room.filter(
        hotel__location__icontains=location_room_query,)
    context = {
        'rooms': query_set
    }
    print(query_set)

    return render(request, 'home.html', context)


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
