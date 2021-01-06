from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    
    path('services/', views.service, name='service'),
    path('shoplist/', views.shoplist, name='shoplist'),
]
