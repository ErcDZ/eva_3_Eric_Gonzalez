from django.contrib import admin
from .models import Editoriale, Comic, Reserva

# Register your models here.
class EditorialAdmin(admin.ModelAdmin):
    list_display = ['nombre']

class ComicAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'precio', 'stock', 'disponible']

class ReservaAdmin(admin.ModelAdmin):
    list_display = ['titulo_identificador', 'correo', 'rut', 'fecha_reserva']

admin.site.register(Editoriale, EditorialAdmin)
admin.site.register(Comic, ComicAdmin)
admin.site.register(Reserva, ReservaAdmin)