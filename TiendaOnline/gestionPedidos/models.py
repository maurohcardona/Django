from django.db import models

# Create your models here.

class Clients(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, verbose_name='The address')
    email = models.EmailField(blank=True, null=True)
    tel = models.CharField('Telephone',max_length=10)
    
    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    price = models.IntegerField()
    
    def __str__(self):
        return f'The product name is {self.name}, the seccion is {self.seccion}, and the price is {self.price}'
    
class Orders(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()
    
    
    