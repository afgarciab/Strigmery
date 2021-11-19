from django import forms
from .models import persona

class personaForm(forms.ModelForm):
    class Meta:
        model = persona
        fields = [
            'nombre',
            'direccion',
            'login',
            'password',
        ]

        labels = {
            'nombre': 'Nombre',
            'direccion': 'Direccion',
            'login': 'Login',
            'password': 'Password',
        }