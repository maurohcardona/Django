from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.shortcuts import render


def salute(request):
    name = "Jhon"
    lastname = "Turnner"
    topics = ["Templates", "Models", "Forms", "Views", "Deploy"]
    return render(request, "miplantilla.html", {"person_name": name, "person_lastname": lastname, "Topics": topics})


def farewell(request):
    return HttpResponse("By my friends")

 
def home(request):
    return HttpResponse("home")

def current_date(request):
    date = datetime.datetime.now()
    return HttpResponse (f"Current date: {date}")

def age_calculator(request,age, year):
    period = year - 2024
    future_age = age + period
    return HttpResponse(f'The age in {year} will be {future_age}')

def c_course(request):
    date = datetime.datetime.now()
    return render(request, "Ccourse.html", {"damefecha": date})

def css_course(request):
    date = datetime.datetime.now()
    return render(request, "csscourse.html", {"damefecha": date})
    