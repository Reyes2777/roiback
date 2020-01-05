import json
import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings

from .models import Hotel, Room, Reservation
from accounts.models import CustomUser
from .utils import is_valid_queryparam, normalize_string


def filter_view(request):
    query_set = Room.objects.all()
    today = datetime.date.today()
    reservations = Reservation.objects.all()
    location_room_query = request.GET.get('location_room')
    capacity_room_query = request.GET.get('capacity_room')
    date_in_query = request.GET.get('date_in')
    date_out_query = request.GET.get('date_out')

    if is_valid_queryparam(location_room_query):
        query_set = query_set.filter(
            hotel__location__icontains=normalize_string(location_room_query),
            hotel__active=True,
            active=True
        )

    if is_valid_queryparam(capacity_room_query):
        query_set = query_set.filter(
            capacity=capacity_room_query,)
    if is_valid_queryparam(date_in_query) and is_valid_queryparam(date_out_query):
        reservations = reservations.filter(
            Q(date_of_enter__range=(date_in_query, date_out_query)) |
            Q(date_of_exit__range=(date_in_query, date_out_query)))
        list_reservation = []
        for reservation in reservations:
            list_reservation.append(reservation.reserved_room.id)
        query_set = query_set.exclude(id__in=list_reservation)

    context = {
        'rooms': query_set,
        'today': today.strftime('%Y-%m-%d'),
        'max_day': (today + datetime.timedelta(days=365)).strftime('%Y-%m-%d')
    }
    print(query_set)

    return render(request, 'home.html', context)


def reservation_view(request, room):
    user = request.POST.get('user')
    room = room
    date_enter = request.POST.get('date_of_enter')
    date_exit = request.POST.get('date_of_exit')
    if is_valid_queryparam(user):
        user = CustomUser.objects.get(id=int(user))

    if is_valid_queryparam(room):
        room = Room.objects.get(id=int(room))
    if user and room:
        try:
            reservation = Reservation(user=user, reserved_room=room, date_of_enter=date_enter, date_of_exit=date_exit)
            reservation.save()
            subject = 'ROIBACK Your Reservation has been Confirmed'
            message = '{} {} Tu reservación ha sido confirmada en el hotel {} para fecha de ingreso {} con salida {}'.format(
                user.first_name, user.last_name, room.hotel.name, date_enter, date_exit
            )
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('home')
        except Exception as e:
            print(HttpResponse(json.dumps({'mensaje': e}), content_type='application/json'))

    return render(request, 'booking/form-reservation.html', )


def details_admin(request):

    rooms = Room.objects.all()
    hotels = Hotel.objects.all()

    context = {
        'rooms': rooms,
        'hotels': hotels
    }
    return render(request, 'booking/details.html', context)


class HotelList(ListView):
    model = Hotel
    template_name = 'booking/home.html'


class HotelCreate(CreateView):
    model = Hotel
    template_name = 'booking/form-hotel.html'
    success_url = reverse_lazy('details')
    fields = ['name', 'description', 'location', 'picture', 'active']


class HotelUpdate(UpdateView):
    model = Hotel
    template_name = 'booking/form-hotel.html'
    success_url = reverse_lazy('details')
    fields = ['name', 'description', 'location', 'picture', 'active']


class HotelDelete(DeleteView):
    model = Hotel
    template_name = 'booking/confirm-delete.html'
    success_url = reverse_lazy('details')


class RoomCreate(CreateView):
    model = Room
    template_name = 'booking/form-room.html'
    success_url = reverse_lazy('details')
    fields = ['hotel', 'number_room', 'description', 'capacity', 'room_type', 'price', 'picture', 'active']


class RoomUpdate(UpdateView):
    model = Room
    template_name = 'booking/form-room.html'
    success_url = reverse_lazy('details')
    fields = ['hotel', 'number_room', 'description', 'capacity', 'room_type', 'price', 'picture', 'active']


class RoomDelete(DeleteView):
    model = Room
    template_name = 'booking/confirm-delete.html'
    success_url = reverse_lazy('details')


class ReservationCreate(CreateView):
    model = Reservation
    template_name = 'booking/form-reservation.html'
    success_url = reverse_lazy('home')
    fields = ['user', 'reserved_room', 'date_of_enter', 'date_of_exit', ]
