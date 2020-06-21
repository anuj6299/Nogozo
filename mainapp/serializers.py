from rest_framework import serializers
from .models import Profile, Service, City, Area, Item, Order

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields ='__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields ='__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields ='__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields ='__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields ='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields ='__all__'