from ..models import Pedido

def get_pedidos():
    pedidos = Pedido.objects.all()
    return pedidos

def get_pedido(id):
    pedido = Pedido.objects.raw("SELECT * FROM pedidos_pedido WHERE id=%s" % id)[0]
    return pedido



def create_pedido(form):
    pedido = form.save()
    pedido.save()
    return ()