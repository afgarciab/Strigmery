from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.pedidos_view, name='pedidos_view'),
    path('<int:pk>', views.pedido_view, name = 'pedido_view'),
]