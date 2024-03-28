from django.shortcuts import render
from .forms import Formulario_contacto

# Create your views here.

def contacto(request):
    
    formulario_contacto = Formulario_contacto()
    
    return render(request, 'contacto.html', {'mi_formulario': formulario_contacto})