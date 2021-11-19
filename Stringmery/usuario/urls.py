from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

urlpatterns = [
    path('usuarios/', views.usuario_list, name='usuarioList'),
    path('usuario/<id>', views.single_usuario, name='singleUsuario'),
    path('usuariocreate/', csrf_exempt(views.usuario_create), name='usuarioCreate'),
]