# apps/pages/views.py

from django.shortcuts import render

def home_view(request):
    # Mengarahkan render ke file template yang baru dibuat
    return render(request, 'pages/home.html')
