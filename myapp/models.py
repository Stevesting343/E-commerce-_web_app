from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Extend_User_Db(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=False)
    type_user = models.CharField(max_length=20)

    
