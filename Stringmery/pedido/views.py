from django.shortcuts import render
from .logic import pedido_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def pedidos_view(request):
    if request.method =='GET':
        id = request.GET.get("id", None)
        if id:
            pedido = vl.get_pedido(id)
            pedido_dto = serializers.serialize('json', [pedido,])
            return HttpResponse( pedido_dto, 'application/json')
        else:
            pedidos = vl.get_pedidos()
            pedidos_dto = serializers.serialize('json', pedidos)
            return HttpResponse(pedidos_dto, 'application/json')

    if request.method == 'POST':
        pedido = vl.create_pedido(json.loads(request.body))
        pedido_dto = serializers.serialize('json', [pedido,])
        return HttpResponse(pedido_dto, 'application/json')


@csrf_exempt
def pedido_view(request, pk):
    if request.method == 'GET':
        pedido_dto = vl.get_pedido(pk)
        pedido = serializers.serialize('json', [pedido_dto,])
        return HttpResponse(pedido, 'application/json')

    if request.method == 'PUT':
        pedido_dto = vl.update_pedido(pk, json.loads(request.body))
        pedido = serializers.serialize('json', [pedido_dto,])
        return HttpResponse(pedido, 'application/json')
# Create your views here.
