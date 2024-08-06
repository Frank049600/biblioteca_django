from django.shortcuts import render, redirect
from django.urls import reverse
from .models import model_estadias
from .forms import estadias_form
import os
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from static.helpers import file_new_name
from django.contrib import messages
from static.utils import dd

# Create your views here.
# def modal_registro(request):
#     return render(request, 'modal_registro.html')

def get_all():
    reporte = model_estadias.objects.all()
    form = estadias_form()

    return [reporte,form]

def index_proyectos(request):
    side_code = 300
    return render(request,'index_proyectos.html',{"reporte":get_all()[0], "form":get_all()[1],"side_code":side_code})

def estadias_registro(request):
    if request.method == 'POST':
        form = estadias_form(request.POST, request.FILES)
        if form.is_valid():
            proyecto = form.cleaned_data['proyecto']
            alumno = form.cleaned_data['alumno']
            asesor_academico = form.cleaned_data['asesor_academico']
            generacion = form.cleaned_data['generacion']
            empresa = form.cleaned_data['empresa']
            asesor_orga = form.cleaned_data['asesor_orga']
            carrera = form.cleaned_data['carrera']
            # name_ref = file_new_name(alumno, request.FILES['reporte'].name)
            name_ref = file_new_name(alumno, form.cleaned_data['reporte'].name)
            # Archivo reporte
            fs = FileSystemStorage()
            reporte = fs.save(name_ref, form.cleaned_data['reporte'])
            # reporte = fs.save(name_ref, request.FILES['reporte'])
            proyectos=model_estadias.objects.create(
                    proyecto = proyecto,
                    alumno = alumno ,
                    asesor_academico = asesor_academico,
                    generacion = generacion,
                    empresa = empresa,
                    asesor_orga = asesor_orga,
                    carrera = carrera,
                    reporte = reporte
            )
            messages.add_message(request, messages.SUCCESS, 'Registro agregado')
            return redirect('proyectos')
            # return redirect('proyectos')
        else:
            # Si el formulario no es válido, vuelve a renderizar el formulario con errores
            form = estadias_form()
    else:
        form = estadias_form()
        messages.add_message(request, messages.ERROR, '¡Algo salio mal!')
        return redirect('proyectos')

# Función para mostrar file report
def view_report(request, report_rute):
    id_reporte = model_estadias.objects.filter(reporte=report_rute).first()
    side_code = 301
    if report_rute != '':
        ruta = settings.MEDIA_URL + report_rute
    else:
        ruta = ''
    return render(request, 'iframe_pdf.html', {'reporte': ruta, "side_code":side_code, "alumno":id_reporte})

def servir_pdf(request, report_rute):
    file_path = os.path.join(settings.MEDIA_ROOT, report_rute)
    response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mi_documento.pdf"'
    return response