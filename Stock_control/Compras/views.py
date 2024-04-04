from django.shortcuts import render, redirect
from .models import Proveedor, Producto
from .forms import Formulario_proveedor, Formulario_producto
from django.urls import reverse

def crear_proveedor(request):
    
    formulario_proveedor = Formulario_proveedor()
    
    if request.method == 'POST':
        
        formulario_proveedor = Formulario_proveedor(data=request.POST)
        
        if formulario_proveedor.is_valid():
            
            nombre = request.POST.get('nombre')
            
            apellido = request.POST.get('apellido')
            
            dni = request.POST.get('dni')
            
            Proveedor.objects.create(nombre = nombre, apellido = apellido, dni = dni)
            
            return redirect(reverse('crear_proveedor') + '?valido')
        
    proveedores = Proveedor.objects.all()
    
    return render(request, 'crear_proveedor.html', {'mi_formulario': formulario_proveedor, 'proveedores': proveedores})


def crear_producto(request):
    
    formulario_producto = Formulario_producto()
    
    if request.method == 'POST':
        
        formulario_producto = Formulario_producto(data=request.POST)
        
        if formulario_producto.is_valid():
            
            nombre = request.POST.get('nombre')
            
            precio = request.POST.get('precio')
            
            stock = request.POST.get('stock_actual')
            
            proveedor_id = request.POST.get('proveedor')
            
            proveedor = Proveedor.objects.get(id=proveedor_id)
            
            Producto.objects.create(nombre = nombre, precio = precio, stock_actual = stock, proveedor = proveedor)
            
            return redirect(reverse('crear_producto') + '?valido')
    
    productos = Producto.objects.all()
    
    return render(request, 'crear_producto.html', {'mi_formulario': formulario_producto, 'productos': productos})

def eliminar_producto(request, producto_id):
    
    producto = Producto.objects.get(id=producto_id)
    
    producto.delete()
    
    return redirect('crear_producto')   

def eliminar_proveedor(request, proveedor_id):
    
    proveedor = Proveedor.objects.get(id=proveedor_id)
    
    proveedor.delete()
    
    return redirect('crear_proveedor')   

def home(request):
    
    return render(request, 'home.html')
