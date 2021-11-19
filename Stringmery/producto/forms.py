from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'comercio1',
            'imagen',
            'pedido',
            'descripcion',
            'cantidad',
            'tiempo_alistamiento',
            'tiempo_preparacion',
            'tiempo_despacho',
        ]

        labels = {
            'comercio1' : 'Comercio1',
            'imagen' : 'Imagen',
            'pedido' : 'Pedido',
            'descripcion' : 'Descripcion',
            'cantidad' : 'Cantidad',
            'tiempo_alistamiento': 'Tiempo_alistamiento',
            'tiempo_preparacion': 'Tiempo_preparacion',
            'tiempo_despacho': 'Tiempo_despacho',
        }