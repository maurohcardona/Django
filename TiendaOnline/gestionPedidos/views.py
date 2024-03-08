from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Products
from django.conf import settings
from django.core.mail import send_mail 
from gestionPedidos.forms import Formulario_contacto

# Create your views here.

def busqueda_productos(request):
    
    return render(request, "busqueda_productos.html")


def buscar(request):
    
    if request.GET.get('prd'):
        #mensaje = f"Articulo buscado: {request.GET.get('prd')}" 
        producto = request.GET.get('prd')
        articulos = Products.objects.filter(name__icontains = producto)
        return render(request, "resultados_busqueda.html", {"articulos": articulos, "query": producto})
    else:
        mensaje = 'No has introducido nada'
    
    return HttpResponse(mensaje)

# FORMA MANUAL

#def contacto(request):
    
    
    # if request.method == "POST":
        
    #     subject = request.POST.get('asunto')
        
    #     message = request.POST.get('mensaje') + " " + request.POST.get('email')
        
    #     email_from = settings.EMAIL_HOST_USER
        
    #     recipient_list = ["maurohcardona@gmail.com"]
        
    #     send_mail(subject, message, email_from, recipient_list)
        
    #     return render(request, "gracias.html")
    
    # return render(request, "contacto.html")
    
def contacto(request):
    
    if request.method == "POST":
        
        mi_formulario = Formulario_contacto(request.POST)
        
        if mi_formulario.is_valid():
            
            inf_form = mi_formulario.cleaned_data
            
            send_mail(inf_form["asunto"], inf_form["mensaje"], inf_form.get("email",""),["maurohcardona@gmail.com"],)
            
            return render(request, "gracias.html")
        
    else:
        
        mi_formulario = Formulario_contacto()
        
    return render(request, "formulario_contacto.html", {"form": mi_formulario})