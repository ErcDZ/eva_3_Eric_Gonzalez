
from django import forms

class formReserva(forms.Form):

    id_reserva = forms.CharField(widget=forms.HiddenInput)
    rut_Cliente  = forms.CharField()
    email    = forms.CharField()
    cantidad  = forms.IntegerField()
    codigo   = forms.CharField()

    id_reserva.widget.attrs.update({'class': 'form-control'})
    rut_Cliente.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    cantidad.widget.attrs.update({'class': 'form-control'})
    codigo.widget.attrs.update({'class': 'form-control'})