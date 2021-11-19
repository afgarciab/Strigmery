from ..models import Producto

def get_productos():
    producto = Producto.objects.all()
    return producto

def get_producto(id):
    producto = Producto.objects.raw("SELECT * FROM  productos_producto WHERE id=%s" % id)[0]
    return producto

def create_producto(form):
    producto = form.save()
    producto.save()
    return ()