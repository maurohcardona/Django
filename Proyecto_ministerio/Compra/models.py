from django.db import models

class Tareas(models.Model):
    
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    
        
    def __str__(self):
        return self.titulo
