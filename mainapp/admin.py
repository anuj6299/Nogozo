from django.contrib import admin
from .models import City, Area, Shop, Item, Feedback, MerchantFeedback, Merchant, Category, Sets

admin.site.register(Feedback)
admin.site.register(MerchantFeedback)
admin.site.register(Merchant)
admin.site.register(Category)
admin.site.register(Sets)