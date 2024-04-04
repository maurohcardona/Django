from django.urls import path
from Compras import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear_proveedor', views.crear_proveedor, name='crear_proveedor'),
    path('crear_producto', views.crear_producto, name='crear_producto'),
    path('eliminar_producto/<int:producto_id>', views.eliminar_producto, name='eliminar_producto'),
    path('eliminar_proveedor/<int:proveedor_id>', views.eliminar_proveedor, name='eliminar_proveedor'),
]