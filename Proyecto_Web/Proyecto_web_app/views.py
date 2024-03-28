from django.shortcuts import render

def home(request):
    
    return render(request, 'Proyecto_web_app/home.html')


def tienda(request):
    
    return render(request, 'Proyecto_web_app/tienda.html')




