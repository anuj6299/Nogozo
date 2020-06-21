from django.contrib import admin
from .models import Profile, Order, Service, City, Area, Item

admin.site.register(Profile)
admin.site.register(Service)
admin.site.register(City)
admin.site.register(Area)
admin.site.register(Item)
admin.site.register(Order)