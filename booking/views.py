import json
import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings

from .models import Hotel, Room, Reservation, Guest
from accounts.models import CustomUser
from .utils import is_valid_queryparam, normalize_string


def filter_view(request):
    query_set = Room.objects.filter(active=True,
                                    hotel__active=True)
    today = datetime.date.today()
    reservations = Reservation.objects.all()
    count_reservations = reservations.count()
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
        'qt_reservations': count_reservations,
        'today': today.strftime('%Y-%m-%d'),
        'max_day': (today + datetime.timedelta(days=365)).strftime('%Y-%m-%d')
    }
    print(query_set)

    return render(request, 'home.html', context)


def reservations_view(request, room):
    user = request.POST.get('user')
    today = datetime.date.today()
    date_enter = request.POST.get('date_of_enter')
    date_exit = request.POST.get('date_of_exit')
    context = {
        'today': today.strftime('%Y-%m-%d'),
        'max_day': (today + datetime.timedelta(days=365)).strftime('%Y-%m-%d'),
        'not_validate_dates': False
    }
    if is_valid_queryparam(user):
        user = CustomUser.objects.get(id=int(user))

    if is_valid_queryparam(room):
        room = Room.objects.get(id=int(room))
        context.update({'range': range(int(room.capacity))})

    if user and room:
        if validate_availability_rooms(date_enter, date_exit, user):
            try:
                price_total = calculate_price_total(date_enter, date_exit, room.price)
                reservation = Reservation(user=user,
                                          reserved_room=room,
                                          date_of_enter=date_enter,
                                          date_of_exit=date_exit,
                                          price_total=price_total)
                reservation.save()
                subject = 'ROIBACK Your Reservation has been Confirmed'
                message = '{} {} Tu reservación ha sido confirmada en el hotel {} para fecha de ingreso {} ' \
                          'con salida {}'.format(user.first_name, user.last_name, room.hotel.name, date_enter, date_exit)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail(subject, message, email_from, recipient_list)
                for _id in range(int(room.capacity)):
                    create_guest(request, _id, reservation)
                return redirect('home')
            except Exception as e:
                print(e)
        else:
            context['not_validate_dates'] = True
            return render(request, 'booking/form-reservation.html', context)
    return render(request, 'booking/form-reservation.html', context)


def validate_availability_rooms(date_enter, date_exit, user):
    reservations = Reservation.objects.all()
    print(reservations)
    if datetime.datetime.strptime(date_enter, '%Y-%m-%d') < datetime.datetime.strptime(date_exit, '%Y-%m-%d'):
        try:
            reservations = reservations.filter(
                Q(date_of_enter__range=(date_enter, date_exit)) |
                Q(date_of_exit__range=(date_enter, date_exit)),
                reserved_room__id=int(user.id))
        except Exception as e:
            print(e)
        if reservations:
            return False
        else:
            return True
    else:
        return False


def create_guest(request, _id, reservation):
    first_name = request.POST.get('first_name{}'.format(_id))
    second_name = request.POST.get('second_name{}'.format(_id))
    last_name = request.POST.get('last_name{}'.format(_id))
    last_second_name = request.POST.get('second_last_name{}'.format(_id))
    birthday_date = request.POST.get('birthday_date{}'.format(_id))
    gender = request.POST.get('gender{}'.format(_id))
    identification_number = request.POST.get('identification_number{}'.format(_id))
    identification_type = request.POST.get('identification_type{}'.format(_id))
    mobile_number = request.POST.get('mobile_number{}'.format(_id))
    email = request.POST.get('email{}'.format(_id))

    print(first_name, second_name, last_name, last_second_name, birthday_date, gender, identification_number,
          identification_type, mobile_number, email)

    guest = Guest(
        first_name=first_name, second_name=second_name, last_name=last_name, last_second_name=last_second_name,
        birthday_date=birthday_date, gender=gender, identification_type=identification_type,
        identification_number=identification_number, mobile_number=mobile_number, reservation=reservation,
        email=email
    )
    try:
        guest.save()
    except Exception as e:
        print(e)


def calculate_price_total(date_enter, date_exit, price):
    date_enter = datetime.datetime.strptime(date_enter, '%Y-%m-%d')
    date_exit = datetime.datetime.strptime(date_exit, '%Y-%m-%d')
    days = date_exit - date_enter
    price_total = days.days * price
    print(price_total)
    return price_total


def details_reservation(request, id_reservation):
    reservation = Reservation.objects.get(id=int(id_reservation))
    context = {
        'reservation': reservation,
    }
    return render(request, 'booking/detail-booking.html', context)


def details_admin(request):

    rooms = Room.objects.all()
    hotels = Hotel.objects.all()

    context = {
        'rooms': rooms,
        'hotels': hotels
    }
    return render(request, 'booking/details.html', context)


def reservation_list(request, status):
    reservations = Reservation.objects.all()
    status_reservation(reservations)

    if status != 'all':
        reservations = reservations.filter(
            status=status
        )

    context = {
        'reservations': reservations,
    }
    return render(request, 'booking/bookings.html', context)


def status_reservation(reservations):
    today = datetime.date.today()
    for reservation in reservations:
        if reservation.date_of_exit < today:
            reservation.status = 'INACTIVA'
            reservation.save(update_fields=['status'])
        elif reservation.date_of_enter <= today <= reservation.date_of_exit:
            reservation.status = 'ACTIVA'
            reservation.save(update_fields=['status'])
        elif reservation.date_of_enter > today:
            reservation.status = 'RESERVADA'
            reservation.save(update_fields=['status'])


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


class ReservationDelete(DeleteView):
    model = Reservation
    template_name = 'booking/confirm-delete.html'
    success_url = reverse_lazy('reservations')


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
