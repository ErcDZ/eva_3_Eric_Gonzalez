
from django import forms

class formReserva(forms.Form):

    id_reserva = forms.CharField(widget=forms.HiddenInput)
    nombre_Cliente  = forms.CharField()
    email    = forms.CharField(required=False)
    cantidad  = forms.IntegerField(min_value=1, max_value=3)
    codigo   = forms.CharField(required=False)

    id_reserva.widget.attrs.update({'class': 'form-control'})
    nombre_Cliente.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    cantidad.widget.attrs.update({'class': 'form-control'})
    codigo.widget.attrs.update({'class': 'form-control'})