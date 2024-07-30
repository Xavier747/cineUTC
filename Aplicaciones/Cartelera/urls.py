#configuradndo redireccionamineto 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    
    # URLs para Género
    path('ListadoGenero', views.ListadoGenero, name='ListadoGenero'),
    path('EliminarGenero/<id>', views.EliminarGenero, name='EliminarGenero'),
    path('nuevoGenero/', views.nuevoGenero, name='nuevoGenero'),
    path('guardarGenero/', views.guardarGenero, name='guardarGenero'),
    path('editarGenero/<id>', views.editarGenero, name='editarGenero'),
    path('procesoActualizacionGenero', views.procesoActualizacionGenero, name='procesoActualizacionGenero'),

    # URLs para País
    path('ListadoPais', views.ListadoPais, name='ListadoPais'),
    path('EliminarPais/<id>', views.EliminarPais, name='EliminarPais'),
    path('nuevoPais/', views.nuevoPais, name='nuevoPais'),
    path('guardarPais/', views.guardarPais, name='guardarPais'),
    path('editarPais/<id>', views.editarPais, name='editarPais'),
    path('procesoActualizacionPais', views.procesoActualizacionPais, name='procesoActualizacionPais'),

    # URLs para Director
    path('ListadoDirector', views.ListadoDirector, name='ListadoDirector'),
    path('EliminarDirector/<id>', views.EliminarDirector, name='EliminarDirector'),
    path('nuevoDirector/', views.nuevoDirector, name='nuevoDirector'),
    path('guardarDirector/', views.guardarDirector, name='guardarDirector'),
    path('editarDirector/<id>', views.editarDirector, name='editarDirector'),
    path('procesoActualizacionDirector', views.procesoActualizacionDirector, name='procesoActualizacionDirector'),

    # URLs para Película
    path('ListadoPelicula', views.ListadoPelicula, name='ListadoPelicula'),
     # URLs para Película
    path('gestionCines', views.gestionCines, name='gestionCines'),
    path('guardarCine/', views.guardarCine, name='guardarCine'),
    path('listadoCines/', views.listadoCines, name='listadoCines'),
]

