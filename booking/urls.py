from django.urls import path
from django.conf.urls import url


from . import views

urlpatterns = [

    url(r'^list$', views.HotelList.as_view(), name='list_hotel'),
    url(r'^detail/(?P<pk>\d+)$', views.HotelDetail.as_view(), name='detail_hotel'),
    url(r'^new-hotel', views.HotelCreate.as_view(), name='new_hotel'),
    url(r'^update-hotel/(?P<pk>\d+)$', views.HotelUpdate.as_view(), name='update_hotel'),
    url(r'^delete-hotel/(?P<pk>\d+)$', views.HotelDelete.as_view(), name='delete_hotel'),

]
