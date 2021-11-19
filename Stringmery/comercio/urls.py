from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

urlpatterns = [
    path('comercios/', views.comercio_list, name='comercioList'),
    path('comercio/<id>', views.single_comercio, name='singleComercio'),
    path('comerciocreate/', csrf_exempt(views.comercio_create), name='comercioCreate'),
]