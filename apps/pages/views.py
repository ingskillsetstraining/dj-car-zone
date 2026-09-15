# apps/pages/views.py

from django.shortcuts import render

def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def cars_view(request):
    return render(request, 'pages/cars.html')

def services_view(request):
    return render(request, 'pages/services.html')

def contact_view(request):
    return render(request, 'pages/contact.html')
