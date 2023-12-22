from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Extend_User_Db(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=False)
    type_user = models.CharField(max_length=20)

class personal_info(models.Model): 
    u_id = models.OneToOneField(User,on_delete=models.CASCADE,null=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=10)
    pincode = models.CharField(max_length=6)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    address = models.CharField(max_length=100)



