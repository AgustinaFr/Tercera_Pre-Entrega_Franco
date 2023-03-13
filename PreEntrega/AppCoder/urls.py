from django.urls import path
from AppCoder import views

urlpatterns = [
   path('', views.inicio),
    path ('clientes', views.clientes),
    path('libros', views.libros),
    path('generos', views.generos),
    #path('clienteFormulario', views.clienteFormulario),
    #path('libroFormulario', views.libroFormulario),
    #path('generoFormulario', views.generoFormulario),
    path('busquedaAutor', views.busquedaAutor),
    path('buscar/', views.buscar),

  #  path('', views.inicio, name='Inicio'),
  #  path ('clientes', views.clientes, name='Clientes'),
  #  path('libros', views.libros, name='Libros'),
  #  path('generos', views.generos, name='Generos')
  #  path('FormularioClientes', views.FormularioClientes, name='FormularioCliente')
]
