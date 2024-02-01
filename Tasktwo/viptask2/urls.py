# django_app/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from five.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login_page'),
    path('register/', register, name='register'),
    path('logout/', logout_page, name='logout_page'),
    path('user-form/', user_form_view, name='user_form_view'),
    path('address-form/', address_form_view, name='address_form_view'),
    path('edu-form/', edu_form_view, name='edu_form_view'),
    path('interest-form/', interest_form_view, name='interest_form_view'),
    path('user-details/', user_details_view, name='user_details_view'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
