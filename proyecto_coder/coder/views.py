from django.shortcuts import render
from django.http import HttpResponse
from coder.models import Curso, Estudiante, Profesor, Entregable
# Create your views here.



def inicio(request):
    return render(request, "coder/index.html", {"mensaje":"La comisión 40150 es la mejor!"})

def estudiante(request):
    return HttpResponse("Vista de estudiante")

def profesor(request):
    profesor = Profesor(nombre= "Leonel", apellido="Gareis", email="example@example.com", profesion="Cloud Developer")
    profesor.save()

    return HttpResponse("Profesor agregado")

def entregable(request):
    return HttpResponse("Vista de entregable")

def cursos(request):

    cursos = Curso.objects.all()

    return render(request, "coder/cursos.html", {"cursos":cursos})
