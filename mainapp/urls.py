from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


app_name = 'mainapp'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('area/', views.area, name='area'),
    path('city/', views.city, name='city'),
    path('items/<str:user>/', views.items, name="items"),
    path('orders/<str:user>/', views.orders, name="orders"),
    path('order/', views.order, name="order"),
    path('profile/', views.profile, name="profile"),
    path('profile/<int:id>/', views.update_profile, name="update_profile"),
    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),

]
