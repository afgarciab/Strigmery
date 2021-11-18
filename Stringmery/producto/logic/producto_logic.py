from ..models import Producto

def get_productos():
    producto = Producto.objects.all()
    return producto

def get_producto(var_pk):
    producto = Producto.objects.get(pk=var_pk)
    return producto

def update_producto(var_pk, new_var):
    producto = get_producto(var_pk)
    producto.name = new_var["name"]
    producto.save()
    return producto

def create_producto(var):
    producto = Producto(name=var["name"])
    producto.save()
    return producto