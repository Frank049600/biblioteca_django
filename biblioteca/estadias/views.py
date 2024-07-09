from django.shortcuts import render, redirect,get_object_or_404
from .models import estadias
import os
from pathlib import Path
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from static.helpers import file_new_name
from static.utils import dd
from django.contrib import auth

# Create your views here.
def modal_registro(request):
        return render(request, 'modal_registro.html')

def index_proyectos(request):
        side_code = 300
        reporte = estadias.objects.all()
        return render(request,'index_proyectos.html',{"reporte":reporte, "side_code":side_code})

def vista_alumnos(request):
        reporte = estadias.objects.all()
        return render(request,'vista_alumnos.html',{"reporte":reporte})

def file_update(files):
        reporte = ''
        c_aceptacion = ''
        convenio = ''
        cronograma = ''
        #for file in files:
        #        if file.FILES['reporte']:
        #               reporte = fs.save(file.name, file)
        #        fs = FileSystemStorage()
        #        uploaded_file_url = fs.url(reporte)
        #        return uploaded_file_url

def estadias_registro(request):
            proyecto=request.POST['proyecto']
            alumno=request.POST['alumno']
            asesor_academico=request.POST['asaca']
            generacion=request.POST['generacion']
            empresa=request.POST['empresa']
            asesor_empresarial=request.POST['asemp']
            carrera=request.POST['carrera']
            # Sección de archivos
            # name_ref = []
            # type_files = ['reporte', 'convenio', 'c_aceptacion', 'cronograma']
            # for file in range(0,len(request.FILES)):
            #         name_ref.append(file_new_name(alumno, request.FILES[type_files[file]].name))
            name_ref = file_new_name(alumno, request.FILES['reporte'].name)
            fs = FileSystemStorage()
            # Archivo reporte
            reporte = fs.save(name_ref, request.FILES['reporte'])
            # url_report = fs.url(reportes)
            # reporte = request.FILES['reporte']
            # Archivo Convenio
            # convenio = fs.save('co_' + name_ref[1], request.FILES['convenio'])
            # url_convenio = fs.url(convenio)
            # # Archivo c_aceptacion
            # c_aceptacion = fs.save('ca_' + name_ref[2], request.FILES['c_aceptacion'])
            # url_c_aceptacion = fs.url(c_aceptacion)
            # # Archivo cronograma
            # cronograma = fs.save('cr_' + name_ref[3], request.FILES['cronograma'])
            # url_cronograma = fs.url(cronograma)

            proyectos=estadias.objects.create(
              proyecto= proyecto,
              alumno=alumno ,
              asesor_academico= asesor_academico,
              generacion=generacion,
              empresa= empresa,
              asesor_empresarial=asesor_empresarial,
              carrera=carrera,
              reporte=reporte
              # convenio=url_convenio,
              # c_aceptacion=url_c_aceptacion,
              # cronograma=url_cronograma
            )

            return redirect('proyectos')
            #return HttpResponse(reporte)

def my_view(request,reporte):
        p=get_object_or_404(estadias,reporte=reporte)
        return render(request,'vistaalumnos.html',{'reporte':p})

# Función para mostrar file report
def view_report(request, report_name):
        # BASE_DIR = Path(__file__).resolve().parent.parent
        # MEDIA_URL = '/files/'
        # MEDIA_ROOT = os.path.join(BASE_DIR, 'files/')
        dd(report_name)
        # reporte=estadias.objects.all()
        # return render(request,'tablaformulario.html')
        #print(MEDIA_ROOT)
        #test_file=open(BASE_DIR + reporte)
        ##response = HttpResponse()
        ##response['Content-Type'] = 'application/pdf'
        #return test_file