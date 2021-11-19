from ..models import comercio

def get_comercios():
    comercios = comercio.objects.all()
    return comercios

def get_comercio(id):
    comercioo = comercio.objects.raw("SELECT * FROM comercios_comercio WHERE id=%s" % id)[0]
    return comercioo

def create_comercio(form):
    comercioo = form.save()
    comercioo.save()
    return ()