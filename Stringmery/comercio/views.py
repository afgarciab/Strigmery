



from django.shortcuts import render
from .forms import comercioForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.comercio_logic import create_comercio, get_comercios, get_comercio
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def comercio_list(request):
    comercios = get_comercios()
    context = {
        'comercio_list': comercios
    }
    return render(request, 'comercio/comercios.html', context)

def comercio_create(request):
    if request.method == 'POST':
        form = comercioForm(request.POST)
        if form.is_valid():
            create_comercio(form)
            messages.add_message(request, messages.SUCCESS, 'comercio create successful')
            return HttpResponseRedirect(reverse('comercioCreate'))
        else:
            print(form.errors)
    else:
        form = comercioForm()

    context = {
        'form': form,
    }

    return render(request, 'comercio/comercioCreate.html', context)


@login_required
def single_comercio(request, id=0):
    comercio = get_comercio(id)
    context = {
        'comercio': comercio
    }
    return render(request, 'comercio/comercio.html', context)
