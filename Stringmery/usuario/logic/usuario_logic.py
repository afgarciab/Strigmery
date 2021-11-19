from ..models import usuario

def get_usuarios():
    usuarios = usuario.objects.all()
    return usuarios

def get_usuario(id):
    usuarioo = usuario.objects.raw("SELECT * FROM usuarios_usuario WHERE id=%s" % id)[0]
    return (usuarioo)


def create_usuario(form):
    usuarioo = form.save()
    usuarioo.save()
    return ()