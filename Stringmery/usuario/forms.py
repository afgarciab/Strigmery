from django import forms
from .models import usuario

class usuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = [
            'nombre',
            'dirs',
            'login',
            'password',
            'documento',
        ]

        labels = {
            'nombre' : 'Nombre',
            'dirs' : 'Dirs',
            'login' : 'Login',
            'password' : 'Password',
            'documento' : 'Documento',
        }