from django.shortcuts import render, redirect
from .models import Area, Publico, Curso
from .forms import AreaForm, PublicoForm, CursoForm


def index(request):
    return render(request, 'index.html')

'''

============= ÁREAS =============

'''

def areas(request):
    areas = Area.objects.all()
    contexto = {
        'areas': areas
    }
    return render(request, 'areas.html', contexto)

def area_cadastrar(request):
    form = AreaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('areas')
    contexto = {
        'form': form
    }
    return render(request, 'area_cadastrar.html', contexto)


def area_editar(request, id):
    area = Area.objects.get(pk=id)
    form = AreaForm(request.POST or None, instance=area)
    if form.is_valid():
        form.save()
        return redirect('areas')
    contexto = {
        'form': form
    }
    return render(request, 'area_cadastrar.html', contexto)


def area_remover(request, id):
    area =  Area.objects.get(pk=id)
    area.delete()
    return redirect('areas')


'''

============= PÚBLICOS =============

'''

def publicos(request):
    publicos = Publico.objects.all()
    contexto = {
        'publicos': publicos
    }
    return render(request, 'publicos.html', contexto)

def publico_cadastrar(request):
    form = PublicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('publicos')
    contexto = {
        'form': form
    }
    return render(request, 'publico_cadastrar.html', contexto)


def publico_editar(request, id):
    publico = Publico.objects.get(pk=id)
    form = PublicoForm(request.POST or None, instance=publico)
    if form.is_valid():
        form.save()
        return redirect('publicos')
    contexto = {
        'form': form
    }
    return render(request, 'publico_cadastrar.html', contexto)


def publico_remover(request, id):
    publico =  Publico.objects.get(pk=id)
    publico.delete()
    return redirect('publicos')




'''

============= CURSOS =============

'''

def cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        'cursos': cursos
    }
    return render(request, 'cursos.html', contexto)

def curso_cadastrar(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cursos')
    contexto = {
        'form': form
    }
    return render(request, 'curso_cadastrar.html', contexto)


def curso_editar(request, id):
    curso = Curso.objects.get(pk=id)
    form = CursoForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect('cursos')
    contexto = {
        'form': form
    }
    return render(request, 'curso_cadastrar.html', contexto)


def curso_remover(request, id):
    curso =  Curso.objects.get(pk=id)
    curso.delete()
    return redirect('cursos')

