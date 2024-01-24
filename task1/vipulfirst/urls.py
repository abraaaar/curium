# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from home.views import *
from webpage.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('receipes/', receipes, name="receipes"),
    path('delete/<int:id>/', delete, name="delete_receipe"),
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),
    path('register/', register, name="register"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
