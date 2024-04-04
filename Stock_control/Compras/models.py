from django.db import models

from django.db import models


class Proveedor(models.Model):
    
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    dni = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'
        
    def __str__(self):
        return self.nombre



class Producto(models.Model):
    
    nombre = models.CharField(max_length = 15)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        
    def __str__(self):
        return self.nombre

