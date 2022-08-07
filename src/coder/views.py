from django.shortcuts import render
from django.http import HttpResponse
from coder.models import Curso, Estudiante, Profesor, Entregable
from coder.forms import CursoFormulario, ProfesorFormulario
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


def crear_curso(request):

    if request.method == "GET":
        formulario = CursoFormulario()
        return render(request, "coder/formulario.html", {"formulario":formulario})
    else:

        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            nombre = data.get("nombre")
            camada = data.get("camada")
            curso = Curso(nombre=nombre, camada=camada)

            curso.save()

            return render(request, "coder/index.html")
        
        else:
            return HttpResponse("Formulario no valido")

def crear_profesor(request):

    if request.method == "GET":
        formulario = ProfesorFormulario()
        return render(request, "coder/formulario.html", {"formulario":formulario})
    else:

        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            nombre = data.get("nombre")
            apellido = data.get("apellido")
            email = data.get("email")
            profesion = data.get("profesion")
            profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)

            profesor.save()

            return render(request, "coder/index.html")
        
        else:
            return HttpResponse("Formulario no valido")

def formulario_busqueda(request):
    return render(request, "coder/formulario_busqueda.html")

def buscar(request):

    curso_nombre = request.GET.get("curso", None)

    if not curso_nombre:
        return HttpResponse("No indicaste ningun nombre")

    cursos_lista = Curso.objects.filter(nombre__icontains=curso_nombre)
    return render(request, "coder/resultado_busqueda.html", {"cursos": cursos_lista})
