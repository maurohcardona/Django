from django.shortcuts import render, HttpResponse
from .models import Tareas

def crear_tarea(request):
    
    if request.method == 'POST':
        
        tarea = request.POST.get('titulo')
        
        descripcion = request.POST.get('descripcion')
        
        Tareas.objects.create(titulo = tarea, descripcion = descripcion)
        
        lista_tareas = Tareas.objects.all()
        
        return render(request, 'lista_tareas.html', {'tareas': lista_tareas})
    
    else:
        
        return render(request, 'crear_tarea.html')
    
    
def ver_tareas(request):
    
    lista_tareas = Tareas.objects.all()
        
    return render(request, 'lista_tareas.html', {'tareas': lista_tareas})
    
        
        
        
    


