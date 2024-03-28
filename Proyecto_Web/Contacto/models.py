from django.db import models

# Create your models here.
class Contacto(models.Model):
    
    nombre = models.CharField(max_length=20),
    
    email = models.EmailField(max_length=15),
    
    mensaje = models.CharField(max_length=50),
    
    created = models.DateTimeField(auto_now_add=True),
    
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'contacto'
        
        verbose_name_plural = 'contactos'
        
    def __str__(self):
        
        return self.nombre
        
    