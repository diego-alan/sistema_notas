from django.db import models
from.validators import validar_maximo
from django.core.validators import EmailValidator

class Curso(models.Model):
    nombre_curso= models.CharField(max_length=255, unique=True)
    codigo= models.IntegerField()

    def __str__(self):
       return f"{self.nombre_curso} - {self.codigo}"    

class Materia(models.Model):
    nombre_materia= models.CharField(max_length=255, unique=True)
    docente= models.CharField(max_length=255, unique=True)
    curso= models.ForeignKey(Curso, on_delete=models.CASCADE) 

    def __str__(self):
       return f"{self.nombre_materia} - {self.docente}  {self.curso}" 


      
class Estudiante(models.Model):
   
    nombres= models.CharField(max_length=255, unique=True)
    apellidoss= models.CharField(max_length=255, unique=True)
    carnet_identidad= models.IntegerField()
    correo = models.EmailField(max_length = 254, validators=[EmailValidator('no es imail valido, vuelva a intentarlo')])
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE) 
    materia= models.ForeignKey(Materia, on_delete=models.CASCADE)

    def __str__(self):
       return f"{self.nombres} - {self.apellidoss}"   

class NotasMateria(models.Model):
    estudiante= models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    examen= models.DecimalField(decimal_places=2, max_digits=5, validators=[validar_maximo,])
    trabajo= models.DecimalField(decimal_places=2, max_digits=5, validators= [validar_maximo,])
    final= models.DecimalField(decimal_places=2, max_digits=5)

    disponible = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f"{self.estudiante} - {self.final}" 