"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto1.views import salute, farewell, home, current_date, age_calculator, c_course, css_course

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salute/', salute),
    path('farewell/', farewell),
    path('home/', home),
    path('fecha/', current_date),
    path('age/<int:age>/<int:year>', age_calculator),
    path('ccourse/', c_course),
    path('csscourse/', css_course)
]
