from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('<int:id>/', views.booking_detail, name='booking_detail'),
    path('new/', views.BookingForm, name='booking_form'),
    path('<int:id>/edit/', views.BookingForm, name='booking_edit'),]
