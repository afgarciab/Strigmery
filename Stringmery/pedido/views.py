


from django.shortcuts import render
from .forms import PedidoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.pedido_logic import create_pedido, get_pedidos, get_pedido
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def pedido_list(request):
    pedidos = get_pedidos()
    context = {
        'pedido_list': pedidos
    }
    return render(request, 'pedido/pedidos.html', context)

def pedido_create(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            create_pedido(form)
            messages.add_message(request, messages.SUCCESS, 'pedido create successful')
            return HttpResponseRedirect(reverse('pedidoCreate'))
        else:
            print(form.errors)
    else:
        form =PedidoForm()

    context = {
        'form': form,
    }

    return render(request, 'pedido/pedidoCreate.html', context)


@login_required
def single_pedido(request, id=0):
    pedido = get_pedido(id)
    context = {
        'pedido': pedido
    }
    return render(request, 'pedido/pedido.html', context)
