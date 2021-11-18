from .logic import producto_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Create your views here.
@csrf_exempt
def productos_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            producto = vl.get_producto(id)
            producto_dto = serializers.serialize('json', [producto, ])
            return HttpResponse(producto_dto, 'application/json')
        else:
            productos = vl.get_productos()
            productos_dto = serializers.serialize('json', productos)
            return HttpResponse(productos_dto, 'application/json')

    if request.method == 'POST':
        producto = vl.create_producto(json.loads(request.body))
        producto_dto = serializers.serialize('json', [producto, ])
        return HttpResponse(producto_dto, 'application/json')


@csrf_exempt
def producto_view(request, pk):
    if request.method == 'GET':
        producto_dto = vl.get_producto(pk)
        producto = serializers.serialize('json', [producto_dto, ])
        return HttpResponse(producto, 'application/json')

    if request.method == 'PUT':
        producto_dto = vl.update_producto(pk, json.loads(request.body))
        producto = serializers.serialize('json', [producto_dto, ])
        return HttpResponse(producto, 'application/json')





