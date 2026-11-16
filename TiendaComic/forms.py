
from django import forms

class formReserva(forms.Form):

    id_reserva = forms.CharField()
    rutCliente  = forms.CharField()
    emailCliente    = forms.CharField()
    cantidadEjemplares  = forms.IntegerField()
    codigoReserva   = forms.CharField()