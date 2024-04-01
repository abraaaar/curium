# django_app/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from five.views import *

urlpatterns = [
    path('', index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
