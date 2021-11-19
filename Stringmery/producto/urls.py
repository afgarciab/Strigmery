from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

urlpatterns = [
    path('productos/', views.producto_list, name='productoList'),
    path('producto/<id>', views.single_producto, name='singleProducto'),
    path('productocreate/', csrf_exempt(views.producto_create), name='productoCreate'),
]