from django import forms
from .models import  Curso, Materia,Estudiante,NotasMateria

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = "__all__"

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = "__all__"

class NotasMateriaForm(forms.ModelForm):
    class Meta:
        model = NotasMateria
        fields = "__all__"
