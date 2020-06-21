from django.shortcuts import render,redirect , get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import City, Area, Item, Service, Profile, Order
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer, OrderSerializer, ServiceSerializer, CitySerializer, AreaSerializer, ItemSerializer

@api_view(['GET'])
def index(request):
    context = {
        'user list and sigup' : '/users',
        'login' : '/token/login',
        'logout' : '/token/logout',
        'service list' : '/service/',
        'area list' : '/area',
        'city list' : '/city',
        'items in a shop' : '/items/<user>',
        'order an item' : '/order',
        'order list' : '/orders/user',
        'profile' : '/profile',
        'profile update' : '/profile/<id>',
    }
    return Response(context)

@api_view(['GET'])
def city(request):
    cities = City.objects.all()
    serializer = CitySerializer(cities,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def area(request):
    areas = Area.objects.all()
    serializer = AreaSerializer(areas,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def service(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def items(request, user):
    all_items = Item.objects.all()
    item_list = []
    for item in all_items:
        if str(item.shop) == str(user):
            item_list.append(item)
    serializer = ItemSerializer(item_list,many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def orders(request, user):
    orders = Order.objects.all()
    order_list = []
    for order in orders:
        if str(order.buyer_name) == str(user):
            order_list.append(order)
        elif str(order.merchant_name) == str(user):
            order_list.append(order)
    serializer = OrderSerializer(order_list,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def profile(request):
    profile = Profile.objects.all()
    serializer = ProfileSerializer(profile,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def update_profile(request, id):
    profile = Profile.objects.get(id=id)
    serializer = ProfileSerializer(instance=profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

