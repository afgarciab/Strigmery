from .logic import comercio_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def comercios_view(request):
    if request.method =='GET':
        id = request.GET.get("id", None)
        if id:
            comercio = vl.get_comercio(id)
            comercio_dto = serializers.serialize('json', [comercio,])
            return HttpResponse( comercio_dto, 'application/json')
        else:
            comercios = vl.get_comercios()
            comercios_dto = serializers.serialize('json', comercios)
            return HttpResponse(comercios_dto, 'application/json')

    if request.method == 'POST':
        comercio = vl.create_variable(json.loads(request.body))
        comercio_dto = serializers.serialize('json', [comercio,])
        return HttpResponse(comercio_dto, 'application/json')


@csrf_exempt
def comercio_view(request, pk):
    if request.method == 'GET':
        comercio_dto = vl.get_comercio(pk)
        comercio = serializers.serialize('json', [comercio_dto,])
        return HttpResponse(comercio, 'application/json')

    if request.method == 'PUT':
        comercio_dto = vl.update_comercio(pk, json.loads(request.body))
        comercio = serializers.serialize('json', [comercio_dto,])
        return HttpResponse(comercio, 'application/json')