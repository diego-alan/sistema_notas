from django.contrib import admin
from .models import Curso
from .models import Materia
from .models import Estudiante
from .models import NotasMateria


admin.site.register(Curso)

class MateriaAdmin(admin.ModelAdmin):
    list_display =("nombre_materia", "docente","curso",)
    ordering = ["curso", "nombre_materia",]
    search_fields = ["materia",]

admin.site.register(Materia, MateriaAdmin)


class EstudianteAdmin(admin.ModelAdmin):
    list_display =("nombres", "apellidoss", "carnet_identidad","correo", "curso","materia",)
    ordering = ["apellidoss",]
    search_fields = ["apellidoss",]

admin.site.register(Estudiante, EstudianteAdmin)

class NotasMateriaAdmin(admin.ModelAdmin):
    list_display =("estudiante", "examen", "trabajo","final",)
    ordering = ["estudiante",]
    search_fields = ["estudiante",]

admin.site.register(NotasMateria, NotasMateriaAdmin)


