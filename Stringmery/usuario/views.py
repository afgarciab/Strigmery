from .logic import usuario_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def usuarios_view(request):
    if request.method =='GET':
        id = request.GET.get("id", None)
        if id:
            usuario = vl.get_usuario(id)
            usuario_dto = serializers.serialize('json', [usuario,])
            return HttpResponse( usuario_dto, 'application/json')
        else:
            usuarios = vl.get_usuarios()
            usuarios_dto = serializers.serialize('json', usuarios)
            return HttpResponse(usuarios_dto, 'application/json')

    if request.method == 'POST':
        usuario = vl.create_usuario(json.loads(request.body))
        usuario_dto = serializers.serialize('json', [usuario,])
        return HttpResponse(usuario_dto, 'application/json')


@csrf_exempt
def usuario_view(request, pk):
    if request.method == 'GET':
        usuario_dto = vl.get_usuario(pk)
        usuario = serializers.serialize('json', [usuario_dto,])
        return HttpResponse(usuario, 'application/json')

    if request.method == 'PUT':
        usuario_dto = vl.update_usuario(pk, json.loads(request.body))
        usuario = serializers.serialize('json', [usuario_dto,])
        return HttpResponse(usuario, 'application/json')