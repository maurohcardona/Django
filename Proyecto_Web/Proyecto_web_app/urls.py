from django.urls import path
from Proyecto_web_app import views

urlpatterns = [
    path('  ', views.home, name='Home'),
    path('tienda', views.tienda, name='Tienda'),
]
