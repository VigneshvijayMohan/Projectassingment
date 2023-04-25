from django.db import models

# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.EmailField()

