from django.urls import path
from .views import crea_curso, lista_cursos, profesores, estudiantes, entregables, cursos, inicio

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', crea_curso, name="creacursos"),
    path('lista-cursos/', lista_cursos, name="listacursos"),
    path('cursos/', cursos, name="cursos"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('profesores/', profesores, name="profesores"),
    path('entregables/', entregables, name="entregables"),
    path('', inicio, name="inicio"),
]
