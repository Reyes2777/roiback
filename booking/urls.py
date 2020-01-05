from django.conf.urls import url
from django.contrib.auth.decorators import permission_required


from . import views

urlpatterns = [

    url(r'^detail/(?P<pk>\d+)$', views.HotelDetail.as_view(), name='detail_hotel'),
    url(r'^new-hotel',  permission_required('is_staff')(views.HotelCreate.as_view()), name='new_hotel'),
    url(r'^update-hotel/(?P<pk>\d+)$',  permission_required('is_staff')(views.HotelUpdate.as_view()),
        name='update_hotel'),
    url(r'^delete-hotel/(?P<pk>\d+)$',  permission_required('is_staff')(views.HotelDelete.as_view()),
        name='delete_hotel'),
    url(r'^new-room',  permission_required('is_staff')(views.RoomCreate.as_view()), name='new_room'),
    url(r'^update-room/(?P<pk>\d+)$',  permission_required('is_staff')(views.RoomUpdate.as_view()),
        name='update_room'),
    url(r'^delete-room/(?P<pk>\d+)$',  permission_required('is_staff')(views.RoomDelete.as_view()),
        name='delete_room'),
    url(r'^new-reservation/(?P<room>\w{0,50})/$',  views.reservation_view, name='reservation')
]
