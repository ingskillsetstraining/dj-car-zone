# apps/pages/views.py

from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Hello, World! Welcome to DJ-CAR-ZONE!</h1>")
