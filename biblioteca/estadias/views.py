from django.shortcuts import render, redirect
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

def estadias_registro(request):
             proyecto=request.POST['proyecto']
             alumno=request.POST['alumno']
             asesor_academico=request.POST['asaca']
             generacion=request.POST['generacion']
             empresa=request.POST['empresa']
             asesor_empresarial=request.POST['asemp']
             carrera=request.POST['carrera']
             reporte=request.POST['archivo']
             convenio=request.POST['convenio']
             c_aceptacion=request.POST['c_aceptacion']
             cronograma=request.POST['cronograma']
        
             proyectos=estadias.objects.create(
               proyecto= proyecto,
               alumno=alumno ,
               asesor_academico= asesor_academico,
               generacion=generacion,
               empresa= empresa,
               asesor_empresarial=asesor_empresarial,
               carrera=carrera,
               reporte=reporte,
               convenio=convenio,
               c_aceptacion=c_aceptacion,
               cronograma=cronograma

        )
             return redirect('proyectos')