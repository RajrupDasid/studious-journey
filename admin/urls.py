from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import include
from django.conf import settings
urlpatterns = [
    path('',include("app.urls")),
    path('admin/', admin.site.urls),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
