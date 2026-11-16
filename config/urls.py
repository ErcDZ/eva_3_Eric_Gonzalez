from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from TiendaComic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('reservar/<int:id>/', views.reservar),
]

if settings.DEBUG:
    urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,}),]