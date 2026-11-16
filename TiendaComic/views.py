from django.shortcuts import render
from TiendaComic.models import Comic, Editoriale, Reserva
from TiendaComic.forms import formReserva

# Create your views here.
def index(request):
    disponibilidad = Comic.objects.all();
    data = {'disponibilidad': disponibilidad}
    return render(request, 'index.html', data)

def reservar(request, id):

    form = formReserva()

    form.fields['id_reserva'].initial = id

    disponibilidad = Comic.objects.get(id = id)
    data = {'disponibilidad': disponibilidad, 'form': form}
    return render(request, 'reservar.html', data)