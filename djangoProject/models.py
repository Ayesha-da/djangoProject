from django.db import models

class User(models.Model):
    title = models.CharField(max_length=50, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], default='Mr')
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=255)

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    stock = models.IntegerField()