from django.db import models

# Create your models here.
class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField( max_length=254)
    tel_phone=models.CharField(max_length=11)
    pwd=models.CharField(max_length=200)
    date_of_birth=models.DateField(auto_now=False)
