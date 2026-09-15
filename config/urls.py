# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.pages.urls')),
]

# Aktifkan penyajian media files hanya selama masa development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# 🔥 TRIK ENTERPRISE: Tangkap request /img/ dari jQuery dan arahkan ke folder static/img
    urlpatterns += static('/img/', document_root=settings.BASE_DIR / 'static/img')