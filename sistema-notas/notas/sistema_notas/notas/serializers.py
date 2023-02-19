from rest_framework import serializers
from.models import Curso, Materia, Estudiante, NotasMateria


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
       model = Materia
       fields = "__all__"

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
       model = Estudiante
       fields = "__all__"

class NotasMateriaSerializer(serializers.ModelSerializer):
    class Meta:
       model = NotasMateria
       fields = "__all__"

