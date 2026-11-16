from django.shortcuts import render
from TiendaComic.models import Comic, Editoriale, Reserva

# Create your views here.
def index(request):
    disponibilidad = Comic.objects.all();
    data = {'disponibilidad': disponibilidad}
    return render(request, 'index.html', data)