from django.contrib import admin
from gestionPedidos.models import Clients, Orders, Products

# Register your models here.

class  ClientsAdmin(admin.ModelAdmin):
    list_display=("name","address","tel")
    search_fields=("name","tel")
    
class OrderAdmin(admin.ModelAdmin):
    list_display=("number", "date", "delivered")
    list_filter=("date",)
    date_hierarchy="date"
    
class ProductsAdmin(admin.ModelAdmin):
    list_filter=("seccion",)

admin.site.register(Clients, ClientsAdmin)    
admin.site.register(Orders, OrderAdmin)
admin.site.register(Products, ProductsAdmin)