# apps/pages/urls.py

from django.urls import path
from .views import home_view, cars_view, about_view, services_view, contact_view

app_name = 'pages'

urlpatterns = [
    path('', home_view, name='home'),
    path('cars/', cars_view, name='cars'),
    path('about/', about_view, name='about'),
    path('services/', services_view, name='services'),
    path('contact/', contact_view, name='contact'),
]
