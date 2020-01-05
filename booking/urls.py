from django.conf.urls import url
from django.contrib.auth.decorators import permission_required, login_required

from booking.views import details_admin


from . import views

urlpatterns = [

    url(r'^details', permission_required('is_staff')(details_admin), name='details'),
    url(r'^new-hotel', permission_required('is_staff')(views.HotelCreate.as_view()), name='new_hotel'),
    url(r'^update-hotel/(?P<pk>\d+)$', permission_required('is_staff')(views.HotelUpdate.as_view()),
        name='update_hotel'),
    url(r'^delete-hotel/(?P<pk>\d+)$', permission_required('is_staff')(views.HotelDelete.as_view()),
        name='delete_hotel'),
    url(r'^new-room', permission_required('is_staff')(views.RoomCreate.as_view()), name='new_room'),
    url(r'^update-room/(?P<pk>\d+)$', permission_required('is_staff')(views.RoomUpdate.as_view()),
        name='update_room'),
    url(r'^delete-room/(?P<pk>\d+)$', permission_required('is_staff')(views.RoomDelete.as_view()),
        name='delete_room'),
    url(r'^new-reservation/(?P<room>\w{0,50})/$', login_required(views.reservation_view),
        name='reservation'),
    url(r'^reservations', login_required(views.reservation_list), name='reservations'),
    url(r'^delete-reservation/(?P<pk>\d+)$', permission_required('is_staff')(views.ReservationDelete.as_view()),
        name='delete_reservation'),
]
