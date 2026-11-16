from django.shortcuts import redirect, render
from TiendaComic.models import Comic, Editoriale, Reserva
from TiendaComic.forms import formReserva
import datetime

# Create your views here.
def index(request):
    disponibilidad = Comic.objects.all();
    data = {'disponibilidad': disponibilidad}
    return render(request, 'index.html', data)

def reservar(request, id):

    form = formReserva()

    form.fields['id_reserva'].initial = id

    if request.method == 'POST':
        form = formReserva(request.POST)
        if form.is_valid():
            disponibilidad = Comic.objects.get(id = id)

            cantidad = form.cleaned_data['cantidad']
            disponibilidad.stock -= cantidad
            disponibilidad.save()

            reserva = Reserva()
            reserva.disponibilidad = disponibilidad
            reserva.nombre_cliente = form.cleaned_data['nombre_Cliente']
            reserva.stock = form.cleaned_data['stock']
            reserva.codigo_reserva = form.cleaned_data['codigo']
            reserva.email = form.cleaned_data['email']
            reserva.fecha_reserva = datetime.datetime.now()

            valor_comic = disponibilidad.precio
            total_original = valor_comic * reserva.stock

            reserva.total_original = total_original
            reserva.save()

            return redirect('/comprobante/' + str(reserva.id))

            
    disponibilidad = Comic.objects.get(id = id)
    data = {'disponibilidad': disponibilidad, 'form': form}
    return render(request, 'reservar.html', data)