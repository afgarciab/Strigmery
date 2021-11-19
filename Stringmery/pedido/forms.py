from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'usuario1',
            'persona1',
            'comercio1',
            'estado',
            'destino',
            'origen',
            'peso',
            'volumen',
        ]

        labels = {
            'usuario1' : 'Usuario1',
            'persona1' : 'Persona1',
            'comercio1' : 'Comercio1',
            'estado' : 'Estado',
            'destino' : 'Destino',
            'origen': 'Origen',
            'peso': 'Peso',
            'volumen': 'Volumen',
        }