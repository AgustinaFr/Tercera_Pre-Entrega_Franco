from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    direccion = forms.CharField()
    telefono = forms.CharField()
    mail = forms.EmailField()

class LibroFormulario(forms.Form):
    titulo = forms.CharField(max_length=60)
    autor = forms.CharField(max_length=40)
    editorial = forms.CharField(max_length=40)

class GeneroFormulario(forms.Form):
    nombre_genero = forms.CharField(max_length=40)