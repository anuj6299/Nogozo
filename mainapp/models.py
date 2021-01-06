from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=20)
    comment = models.TextField()
    
    def __str__(self):
        return self.name


class MerchantFeedback(models.Model):
    shop_name = models.CharField(max_length=120)
    contact_number = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=250)
    comment = models.TextField()
    
    def __str__(self):
        return self.shop_name

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

class Shop(models.Model):
    shop_id = models.IntegerField(primary_key=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=500)

    def __str__(self):
        return self.shop_name

class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=500)

    def __str__(self):
        return self.item_name

class Merchant(models.Model):
    shop_id = models.IntegerField(primary_key=True)
    shop_name = models.CharField(max_length=500)
    shop_address = models.CharField(max_length=500)
    shop_image = models.CharField(max_length=500)

    def __str__(self):
        return self.shop_name

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=500)
    
    def __str__(self):
        return self.category_name

class Sets(models.Model):
    set_id = models.IntegerField(primary_key=True)
    set_topic = models.CharField(max_length=500)
    set_date = models.CharField(max_length=500)
    set_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    set_question1 = models.CharField(max_length=500)
    set_option1a = models.CharField(max_length=500)
    set_option1b = models.CharField(max_length=500)
    set_option1c = models.CharField(max_length=500)
    set_answer1 = models.CharField(max_length=500)
    set_img1 = models.CharField(max_length=500)

    set_question2 = models.CharField(max_length=500)
    set_option2a = models.CharField(max_length=500)
    set_option2b = models.CharField(max_length=500)
    set_option2c = models.CharField(max_length=500)
    set_answer2 = models.CharField(max_length=500)
    set_img2 = models.CharField(max_length=500)

    set_question3 = models.CharField(max_length=500)
    set_option3a = models.CharField(max_length=500)
    set_option3b = models.CharField(max_length=500)
    set_option3c = models.CharField(max_length=500)
    set_answer3 = models.CharField(max_length=500)
    set_img3 = models.CharField(max_length=500)

    set_question4 = models.CharField(max_length=500)
    set_option4a = models.CharField(max_length=500)
    set_option4b = models.CharField(max_length=500)
    set_option4c = models.CharField(max_length=500)
    set_answer4 = models.CharField(max_length=500)
    set_img4 = models.CharField(max_length=500)

    set_question5 = models.CharField(max_length=500)
    set_option5a = models.CharField(max_length=500)
    set_option5b = models.CharField(max_length=500)
    set_option5c = models.CharField(max_length=500)
    set_answer5 = models.CharField(max_length=500)
    set_img5 = models.CharField(max_length=500)

    def __str__(self):
        return self.set_topic
