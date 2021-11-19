from django.shortcuts import render
from .forms import personaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.persona_logic import create_persona, get_personas, get_persona
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def persona_list(request):
    personas = get_personas()
    context = {
        'persona_list': personas
    }
    return render(request, 'persona/personas.html', context)

def persona_create(request):
    if request.method == 'POST':
        form = personaForm(request.POST)
        if form.is_valid():
            create_persona(form)
            messages.add_message(request, messages.SUCCESS, 'persona create successful')
            return HttpResponseRedirect(reverse('personaCreate'))
        else:
            print(form.errors)
    else:
        form = personaForm()

    context = {
        'form': form,
    }

    return render(request, 'persona/personaCreate.html', context)


@login_required
def single_persona(request, id=0):
    persona = get_persona(id)
    context = {
        'persona': persona
    }
    return render(request, 'persona/persona.html', context)
