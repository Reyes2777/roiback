from django.urls import path

from . import views

urlpatterns = [
    path('list-hotel/', views.HotelList.as_view(), name='list_hotel'),
    path('detail-hotel/', views.HotelDetail.as_view(), name='detail_hotel'),
    path('create-hotel/', views.HotelCreate.as_view(), name='create_hotel'),
    path('update-hotel/', views.HotelUpdate.as_view(), name='update_hotel'),
    path('delete-hotel/', views.HotelDelete.as_view(), name='delete_hotel')
]
