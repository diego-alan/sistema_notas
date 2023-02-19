from django.shortcuts import render
from django.http import HttpResponse
from.models import Curso,Materia,Estudiante, NotasMateria
from.forms import MateriaForm, CursoForm, EstudianteForm, NotasMateriaForm
from rest_framework import viewsets,generics
from .serializers import CursoSerializer, MateriaSerializer, EstudianteSerializer, NotasMateriaSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse


def index(request):
    return HttpResponse('lugar de notas')


def sistema(request,name):
    return HttpResponse(f"Bienvenido {name} de Django")

#-----CURSO

def curso(request):
    post_nombre_curso = request.POST.get('nombre_curso')
    if post_nombre_curso:
        q =Curso(curso=post_nombre_curso)
        q.save()

def cursoFormView(request):
    form = CursoForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "from_curso.html", {
        "form": form
})

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


#-----MATERIA


def materiaFormView(request):
    form = MateriaForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "from_materia.html", {
        "form": form
})

#class MateriaViewSet(viewsets.ModelViewSet):
  #  queryset = Materia.objects.all()
  #  serializer_class = MateriaSerializer

class MateriaCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

def materia(request):
    materia= Materia.objects.all()
    return render(request, "materia.html", {
      "materia": materia
    })


#-------ESTUDIANTE
def estudianteFormView(request):
    form = EstudianteForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "from_estudiante.html", {
        "form": form
})

def estudiante(request):
    estudiante= Estudiante.objects.all()
    return render(request, "estudiante.html", {
        "estudiante": estudiante
    })

#class EstudianteViewSet(viewsets.ModelViewSet):
 #   queryset = Estudiante.objects.all()
  #  serializer_class = EstudianteSerializer

class EstudianteCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer



#-----------------NOTAS DE MATERIAS

def notasMateriaFormView(request):
    form = NotasMateriaForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "from_notasMaterias.html", {
        "form": form
})

def notasMateria(request):
    notasMateria= NotasMateria.objects.all()
    return render(request, "notasMateria.html", {
        "notasMateria": notasMateria
    })

@api_view(["GET"])
def notasMateria_count(request):
    try:
        final= NotasMateria.objects.count()
        return JsonResponse({
            "final": final
        },
        safe = False, 
        status=200,
    )

    except Exception as e:
            return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def examen_notasMateria(request):  
    try:
        notasMateria = NotasMateria.objects.filter( estudiante=='pedro')
        return JsonResponse(
            NotasMateriaSerializer(notasMateria, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

   