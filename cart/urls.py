from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:item_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
    path('checkout/', views.checkout, name='cart_checkout'),
    path('success/', views.order_success, name='order_success'),
]
