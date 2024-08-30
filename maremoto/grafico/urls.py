from django.urls import path
from . import views

urlpatterns = [
    path('', views.visualizar_maremoto, name='visualizar_maremoto'),
]
