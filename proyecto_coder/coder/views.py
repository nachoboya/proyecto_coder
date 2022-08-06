from django.shortcuts import render
from django.http import HttpResponse
from coder.models import Curso
# Create your views here.


def lista_cursos(request):

    cursos = Curso.objects.all()
    return HttpResponse(cursos[0].nombre)
