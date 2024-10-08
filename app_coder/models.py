from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} - {self.camada}'
    
    class Meta():
       verbose_name = 'Curso'
       verbose_name_plural = 'Cursos'
       ordering = ('nombre', 'camada',)

         


class Estudiante (models.Model):
    nombre= models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30) 
    email= models.EmailField()
  
    def __str__(self):
     return f'{self.nombre} {self.apellido}'


class Profesor(models.Model):
    nombre= models.CharField(max_length=30) 
    apellido= models.CharField(max_length=30) 
    email= models.EmailField() 
    profesion= models.CharField(max_length=30)


class Entregable(models. Model):
    nombre= models.CharField(max_length=30) 
    fechaDeEntrega = models.DateField() 
    entregado = models.BooleanField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
     return f'{self.nombre}'

















