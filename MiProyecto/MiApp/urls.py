from django.urls import path
from . import views
from .views import *



urlpatterns = [
    path('padre/', views.vista_padre, name='vista_padre'),
    path('insertar_profesor/', views.insertar_profesor, name='insertar_profesor'),
    path('insertar_director/', views.insertar_director, name='insertar_director'),
    path('insertar_preceptor/', views.insertar_preceptor, name='insertar_preceptor'),
    path('exito/', views.exito, name='exito'),
    path('resultados_busqueda/', views.resultados_busqueda, name='resultados_busqueda'),
    path('vista_profesor/', views.vista_profesor, name='vista_profesor'),
    path('vista_director/', views.vista_director, name='vista_director'),
    path('inicio/', views.inicio, name='inicio'), 
]
