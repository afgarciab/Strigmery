from ..models import usuario

def get_usuarios():
    usuarios = usuario.objects.all()
    return usuarios

def get_usuario(var_pk):
    usuarioo = usuario.objects.get(pk=var_pk)
    return usuarioo

def update_usuario(var_pk, new_var):
    usuario = get_usuario(var_pk)
    usuario.name = new_var["name"]
    usuario.save()
    return usuario

def create_usuario(var):
    usuarioo = usuario(name=var["name"])
    usuarioo.save()
    return usuarioo