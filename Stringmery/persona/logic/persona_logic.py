from ..models import persona

def get_personas():
    personas = persona.objects.all()
    return personas

def get_persona(id):
    personaa= persona.objects.raw("SELECT * FROM personas_persona WHERE id=%s" % id)[0]
    return personaa

def create_persona(form):
    personaa = form.save()
    personaa.save()
    return ()