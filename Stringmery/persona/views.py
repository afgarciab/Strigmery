from .logic import persona_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def personas_view(request):
    if request.method =='GET':
        id = request.GET.get("id", None)
        if id:
            persona = vl.get_persona(id)
            persona_dto = serializers.serialize('json', [persona,])
            return HttpResponse( persona_dto, 'application/json')
        else:
            personas = vl.get_personas()
            personas_dto = serializers.serialize('json', personas)
            return HttpResponse(personas_dto, 'application/json')

    if request.method == 'POST':
        persona = vl.create_persona(json.loads(request.body))
        persona_dto = serializers.serialize('json', [persona,])
        return HttpResponse(persona_dto, 'application/json')


@csrf_exempt
def persona_view(request, pk):
    if request.method == 'GET':
        persona_dto = vl.get_persona(pk)
        persona = serializers.serialize('json', [persona_dto,])
        return HttpResponse(persona, 'application/json')

    if request.method == 'PUT':
        persona_dto = vl.update_persona(pk, json.loads(request.body))
        persona = serializers.serialize('json', [persona_dto,])
        return HttpResponse(persona, 'application/json')