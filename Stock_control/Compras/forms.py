from django import forms
from .models import Producto, Proveedor

class Formulario_proveedor(forms.ModelForm):
    
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'dni']
    

class Formulario_producto(forms.ModelForm):
    
   class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock_actual', 'proveedor']