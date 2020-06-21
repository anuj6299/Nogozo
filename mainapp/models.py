from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Profile_category = models.CharField(default='User', max_length=100, blank=True)
    service = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    city = models.CharField(max_length=100, blank=True)
    area = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=500)
    
    def __str__(self):
        return self.city_name

        
class Area(models.Model):
    area_id = models.IntegerField(primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area_name = models.CharField(max_length=500)

    def __str__(self):
        return self.area_name


class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    shop = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=500)
    item_price = models.CharField(max_length=500)
    item_category = models.CharField(max_length=100, blank=True)
    item_availability = models.BooleanField(default=True)

    def __str__(self):
        return self.item_name


class Service(models.Model):
    service_id = models.IntegerField(primary_key=True)
    service_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.service_name


class Order(models.Model):
    oder_id = models.IntegerField(primary_key=True)
    buyer_name = models.CharField(max_length=100, blank=True)
    merchant_name = models.CharField(max_length=100, blank=True)
    order_total = models.CharField(max_length=100, blank=True)
    order_details = models.TextField(blank=True, null=True)
    order_packed = models.BooleanField(default=False)
