from django.db import models
from django.contrib.auth.models import User

class PlantCategory(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='catx')
    def __str__(self):
        return self.name
class Plant(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(PlantCategory, on_delete=models.CASCADE)
    description = models.TextField()
    image=models.ImageField(upload_to='plants')
    price=models.IntegerField(null=True)
    stock=models.IntegerField(null=True)
    def __str__(self):
        return self.name

class CartItems(models.Model):
   
    plant=models.ForeignKey(Plant,on_delete=models.CASCADE, default=0,null=True)
    quantity=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    def __str__(self):
        return self.plant










# Create your models here.

# Create your models here.
