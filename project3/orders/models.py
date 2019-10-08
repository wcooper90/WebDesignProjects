from django.db import models
from django.conf import settings
from jsonfield import JSONField
import json

# Create your models here.

# Admin can add menu objects to page
class Menu(models.Model):
    category = models.CharField(max_length=64)
    smallPrice = models.FloatField(max_length=7)
    largePrice = models.FloatField(max_length=7)
    custom = models.BooleanField(null=True, blank=True)
    toppingPrice = models.FloatField(max_length=7, blank=True, null=True)


# cart is created for each user
class Cart(models.Model):
    items = JSONField()
    addOns = JSONField(null=True, blank=True)

    def add_item(self, item):
        if not self.items:
            self.items = []
        self.items.append(item)
    def addOn(self, addOn, item):
        if not self.addOns:
            self.addOns = {}
        if item not in self.addOns :
            self.addOns[item] = []
        self.addOns[item].append(addOn)
    def removeAll(self):
        self.items = []
        self.addOns = {}


# user profile is created for each user so that they can have a cart associated with them 
class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=64)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

    def get_cart(self):
        return self.cart
