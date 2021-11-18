from ..models import comercio

def get_comercios():
    comercios = comercio.objects.all()
    return comercios

def get_comercio(var_pk):
    comercioo = comercio.objects.get(pk=var_pk)
    return comercioo

def update_comercio(var_pk, new_var):
    comercio = get_comercio(var_pk)
    comercio.name = new_var["name"]
    comercio.save()
    return comercio

def create_variable(var):
    comercioo = comercio(name=var["name"])
    comercioo.save()
    return comercioo