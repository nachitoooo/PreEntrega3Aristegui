from django.shortcuts import render, redirect
from .models import Profesor, Director, Preceptor
from .forms import ProfesorForm, DirectorForm, PreceptorForm

def insertar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = ProfesorForm()
    return render(request, 'MiApp/insertar_profesor.html', {'form': form})


def insertar_director(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = DirectorForm()
    return render(request, 'insertar_director.html', {'form': form})

def insertar_preceptor(request):
    if request.method == 'POST':
        form = PreceptorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = PreceptorForm()
    return render(request, 'insertar_preceptor.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')

def resultados_busqueda(request):
    if request.method == 'POST':
        termino_busqueda = request.POST.get('termino_busqueda', '') 

        resultados_profesores = Profesor.objects.filter(nombre__icontains=termino_busqueda)
        resultados_directores = Director.objects.filter(nombre__icontains=termino_busqueda)
        resultados_preceptores = Preceptor.objects.filter(nombre__icontains=termino_busqueda)

        context = {
            'resultados_profesores': resultados_profesores,
            'resultados_directores': resultados_directores,
            'resultados_preceptores': resultados_preceptores,
        }
        return render(request, 'resultados_busqueda.html', context)
    else:
        return render(request, 'busqueda.html')

def vista_padre(request):
    return render(request, 'MiApp/padre.html')

def vista_profesor(request):
    return render(request, 'MiApp/insertar_profesor.html')

def vista_director(request):
    return render(request, 'MiApp/insertar_director.html')

def inicio(request):
    return render(request, 'MiApp/inicio.html')
