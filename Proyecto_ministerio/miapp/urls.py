from django.urls import path
from miapp import views

urlpatterns = [
    path('crear_tarea', views.crear_tarea, name='crear_tarea'),
    path('lista_tareas/', views.ver_tareas, name='lista_tareas')
]