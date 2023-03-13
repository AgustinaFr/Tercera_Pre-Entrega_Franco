from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *


# Create your views here.

def inicio(request):
  return render (request, 'AppCoder/inicio.html')

#def clientes(request):
#  return render (request, 'AppCoder/clientes.html')

#def libros(request):
#  return render (request, 'AppCoder/libros.html')

#def generos(request):  
#  return render (request, 'AppCoder/generos.html')


#def clienteFormulario(request):
def clientes(request):
  if request.method == 'POST':
    miFormulario = ClienteFormulario(request.POST)
    print(miFormulario)

    if miFormulario.is_valid:
      informacion = miFormulario.cleaned_data
      cliente = Clientes(nombre = informacion['nombre'], apellido = informacion['apellido'], direccion = informacion['direccion'], telefono = informacion['telefono'], mail = informacion['mail'])
      cliente.save()
      return render(request, 'AppCoder/inicio.html')
  else:
    miFormulario = ClienteFormulario()
    #  return render(request, 'AppCoder/clienteFormulario.html', {"miFormulario":miFormulario})
  return render(request, 'AppCoder/clientes.html', {"miFormulario":miFormulario})

#def libroFormulario(request):
def libros(request):
  if request.method == 'POST':
    miFormulario = LibroFormulario(request.POST)
    print(miFormulario)

    if miFormulario.is_valid:
      informacion = miFormulario.cleaned_data
      libro = Libros(titulo = informacion['titulo'], autor = informacion['autor'], editorial = informacion['editorial'])
      libro.save()
      return render(request, 'AppCoder/inicio.html')
  else:
    miFormulario = LibroFormulario()

 # return render(request, 'AppCoder/libroFormulario.html', {"miFormulario":miFormulario})
  return render(request, 'AppCoder/libros.html', {"miFormulario":miFormulario})

#def generoFormulario(request):
def generos(request):
  if request.method == 'POST':
    miFormulario = GeneroFormulario(request.POST)
    print(miFormulario)

    if miFormulario.is_valid:
      informacion = miFormulario.cleaned_data
      genero = Generos(nombre_genero = informacion['nombre_genero'])
      genero.save()
      return render(request, 'AppCoder/inicio.html')
  else:
    miFormulario = GeneroFormulario()

  #return render(request, 'AppCoder/generoFormulario.html', {"miFormulario":miFormulario})
  return render(request, 'AppCoder/generos.html', {"miFormulario":miFormulario})

def busquedaAutor(request):
  return render(request, 'AppCoder/busquedaAutor.html')

def buscar(request):
  if request.GET['autor']:
    autor = request.GET['autor']
    titulos = Libros.objects.filter(autor__icontains=autor)
    return render(request, 'AppCoder/resultadosBusqueda.html',{'titulos':titulos, 'autor':autor})

  else:
    respuesta = 'No se enviaron datos'

  return HttpResponse(respuesta)