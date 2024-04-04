from django.contrib import admin
from .models import Producto, Proveedor

class Proveedor_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
class Producto_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Proveedor, Proveedor_admin)

admin.site.register(Producto, Producto_admin)