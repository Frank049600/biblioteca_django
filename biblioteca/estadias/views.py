from django.shortcuts import render
from .models import estadias
# Create your views here.
def modal_registro(request):
        return render(request, 'modal_registro.html')

def index_proyectos (request):
        reporte=estadias.objects.all()
        return render(request,'tablaformulario.html',{"reporte":reporte})

def vistaalumnos(request):
        reporte=estadias.objects.all()
       
        return render(request,'vistaalumnos.html',{"reporte":reporte})