from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

urlpatterns = [
    path('pedidos/', views.pedido_list, name='pedidoList'),
    path('pedido/<id>', views.single_pedido, name='singlePedido'),
    path('pedidocreate/', csrf_exempt(views.pedido_create), name='pedidoCreate'),
]