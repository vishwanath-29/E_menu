from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class restaurant(models.Model):
    Restaurant_Id=models.ForeignKey(User,on_delete=models.PROTECT)
    Restaurant_name=models.CharField(max_length=50)