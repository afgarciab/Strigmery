from ..models import persona

def get_personas():
    personas = persona.objects.all()
    return personas

def get_persona(var_pk):
    personaa= persona.objects.get(pk=var_pk)
    return personaa

def update_persona(var_pk, new_var):
    persona = get_persona(var_pk)
    persona.name = new_var["name"]
    persona.save()
    return persona

def create_variable(var):
    personaa = persona(name=var["name"])
    personaa.save()
    return personaa