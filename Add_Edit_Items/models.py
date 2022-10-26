from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Food(models.Model):
    Restaurant_ID=models.ForeignKey(User,on_delete=models.PROTECT)
    Food_Name=models.CharField(max_length=30)
    Short_Description=models.CharField(max_length=50)
    is_veg=models.BooleanField()
    is_bestseller=models.BooleanField()
    is_available=models.BooleanField()
    Price=models.FloatField()
    Category=models.CharField(max_length=50)
    
