from django.shortcuts import render
from .forms import ProductoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.producto_logic import create_producto, get_productos, get_producto
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def producto_list(request):
    productos = get_productos()
    context = {
        'producto_list': productos
    }
    return render(request, 'producto/productos.html', context)

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            create_producto(form)
            messages.add_message(request, messages.SUCCESS, 'producto create successful')
            return HttpResponseRedirect(reverse('productoCreate'))
        else:
            print(form.errors)
    else:
        form =ProductoForm()

    context = {
        'form': form,
    }

    return render(request, 'producto/productoCreate.html', context)


@login_required
def single_producto(request, id=0):
    producto = get_producto(id)
    context = {
        'producto': producto
    }
    return render(request, 'producto/producto.html', context)



