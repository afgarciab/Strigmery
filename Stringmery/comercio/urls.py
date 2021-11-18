from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.comercios_view, name='comercios_view'),
    path('<int:pk>', views.comercio_view, name = 'comercio_view'),
]