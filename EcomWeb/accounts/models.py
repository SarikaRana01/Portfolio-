from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    state=models.TextField(null=False,blank=False)
    distt=models.TextField(null=False,blank=False)
    city=models.TextField(null=False,blank=False)
    pincode=models.IntegerField()

    def __str__(self):
        return self.user.username
    

class Phone(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.TextField(null=False,blank=False)

    def __str__(self):
        return self.user.username