from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Libro
from .forms import LibroForm

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def servicios(request):
    return render(request, 'paginas/servicios.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario':formulario})

def editar(request):
    return render(request, 'libros/editar.html')

def eliminar(request, libro_id):
    libro = Libro.objects.get(libro_id = libro_id)
    libro.delete()
    return redirect('libros')
    


