from .logic import usuario_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt



from django.shortcuts import render
from .forms import usuarioForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.usuario_logic import create_usuario, get_usuarios, get_usuario
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def usuario_list(request):
    usuarios = get_usuarios()
    context = {
        'usuario_list': usuarios
    }
    return render(request, 'usuario/usuarios.html', context)

def usuario_create(request):
    if request.method == 'POST':
        form = usuarioForm(request.POST)
        if form.is_valid():
            create_usuario(form)
            messages.add_message(request, messages.SUCCESS, 'usuario create successful')
            return HttpResponseRedirect(reverse('usuarioCreate'))
        else:
            print(form.errors)
    else:
        form = usuarioForm()

    context = {
        'form': form,
    }

    return render(request, 'usuario/usuarioCreate.html', context)


@login_required
def single_usuario(request, id=0):
    usuario = get_usuario(id)
    context = {
        'usuario': usuario
    }
    return render(request, 'usuario/usuario.html', context)
