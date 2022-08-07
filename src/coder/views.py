from django.shortcuts import render
from django.http import HttpResponse
from coder.models import Curso, Estudiante, Profesor, Entregable
# Create your views here.



def inicio(request):
    contexto = {
        "mensaje":"La comisión 40150 es la mejor!",
        "mensaje_bienvenida":"Bienvenid@s!"
    }

    return render(request, "coder/index.html", contexto)

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

    contexto = {
        "mensaje":"Todos nuestros cursos al mejor precio!",
        "mensaje_bienvenida":"Bienvenid@s!",
        "cursos":cursos
    }

    return render(request, "coder/cursos.html", contexto)
