from django.urls import path
from .views import crea_curso, lista_cursos, profesores, estudiantes, entregables, cursos, inicio, curso_formulario, busqueda_camada, buscar_camada

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', crea_curso, name="creacursos"),
    path('lista-cursos/', lista_cursos, name="listacursos"),
    path('cursos/', cursos, name="cursos"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('profesores/', profesores, name="profesores"),
    path('entregables/', entregables, name="entregables"),
    path('inicio/', inicio, name="inicio"),
    path('curso-formulario/', curso_formulario, name="cursoformulario"),
    path('busqueda-camada/', busqueda_camada, name="busquedacamada"),
    path('buscar-camada/', buscar_camada, name="buscarcamada"),


]
