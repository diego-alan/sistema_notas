from django.urls import path, include
from . import views
#from rest_framework.routers import DefaultRouter

#router = DefaultRouter()
#router.register(r"Cursos", views.CursoViewSet)

urlpatterns = [
 
    path("sistema/<str:name>", views.sistema, name="sistema"),   
    path("curso", views.cursoFormView, name ="curso"),
    path("materia", views.materiaFormView, name ="materia"),
    path("estudiante", views.estudianteFormView, name ="estudiante"),
    path("notasMateria", views.notasMateriaFormView, name ="notasMateria"),


    path("curso\crear",views.CursoCreateView.as_view()),
    
    path("materia\crear",views.MateriaCreateView.as_view()),
    
    path("estudiante\crear",views.EstudianteCreateView.as_view()),
    
    path("notasMateria\final",views.notasMateria_count),

    path("notasMateria\filtrar\examen",views.examen_notasMateria, name = "filtrar"),
    #path("", include(router.urls))
   
    path("", views.index, name ="index")
  
]

    