from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

urlpatterns = [
    path('personas/', views.persona_list, name='personaList'),
    path('persona/<id>', views.single_persona, name='singlePersona'),
    path('personacreate/', csrf_exempt(views.persona_create), name='personaCreate'),
]