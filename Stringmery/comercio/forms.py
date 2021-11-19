from django import forms
from .models import comercio

class comercioForm(forms.ModelForm):
    class Meta:
        model = comercio
        fields = [
            'nombre',
            'dirs',
            'login',
            'password',
            'estado',
        ]

        labels = {
            'nombre' : 'Nombre',
            'dirs' : 'Dirs',
            'login' : 'Login',
            'password' : 'Password',
            'estado' : 'Estado',
        }