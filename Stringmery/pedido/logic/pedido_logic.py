from ..models import Pedido

def get_pedidos():
    pedidos = Pedido.objects.all()
    return pedidos

def get_pedido(var_pk):
    pedido = Pedido.objects.get(pk=var_pk)
    return pedido

def update_pedido(var_pk, new_var):
    pedido = get_pedido(var_pk)
    pedido.name = new_var["name"]
    pedido.save()
    return pedido

def create_pedido(var):
    pedido = Pedido(name=var["name"])
    pedido.save()
    return pedido