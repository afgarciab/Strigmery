from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.personas_view, name='personas_view'),
    path('<int:pk>', views.persona_view, name = 'persona_view'),
]