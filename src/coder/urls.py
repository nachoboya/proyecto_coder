from django.urls import path
from coder.views import *

urlpatterns = [
    path("", inicio, name='inicio'),
    path("cursos/", cursos, name='cursos'),
    path("estudiantes/", estudiante, name='estudiantes'),
    path("profesores/", profesor, name='profesores'),
    path("entregables/", entregable, name='entregables'),
    path("curso/crear/", crear_curso, name='curso_crear'),
    path("profesor/crear/", crear_profesor, name='profesor_crear'),
    path("formulario/", formulario_busqueda, name="FormularioBusqueda"),
    path("resultados/", buscar, name="buscar_curso")
]