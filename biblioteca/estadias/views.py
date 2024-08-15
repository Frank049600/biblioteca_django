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
from sito.models import Alumno, AlumnoGrupo, Grupo, Carrera, Usuario, Persona, Periodo
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

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
            matricula = form.cleaned_data['matricula']
            alumno = form.cleaned_data['alumno']
            asesor_academico = form.cleaned_data['asesor_academico']
            generacion = form.cleaned_data['generacion']
            empresa = form.cleaned_data['empresa']
            asesor_orga = form.cleaned_data['asesor_orga']
            carrera = form.cleaned_data['carrera']
            name_ref = file_new_name(alumno, form.cleaned_data['reporte'].name)
            # Archivo reporte
            fs = FileSystemStorage()
            reporte = fs.save(name_ref, form.cleaned_data['reporte'])

            proyectos=model_estadias.objects.create(
                    proyecto = proyecto,
                    matricula = matricula,
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

# Función de búsqueda para retorno de información por búsqueda con matricula
def get_alumno(request):
    matricula = request.GET.get('matricula')
    if matricula:
        cve_persona = ''
        try:
            # alumno_grupo = get_object_or_404(AlumnoGrupo, matricula=matricula)
            alumno_grupo = AlumnoGrupo.objects.filter(matricula=matricula).values_list('cve_grupo', flat=True)
            cve_grupo = alumno_grupo[len(alumno_grupo) - 1]
            grupo = Grupo.objects.get(cve_grupo=cve_grupo)
            carrera = Carrera.objects.get(nombre=grupo.cve_carrera)
            generacion = Alumno.objects.get(matricula=matricula)
            cve_persona = Usuario.objects.get(login=matricula)
            persona = Persona.objects.get(cve_persona=cve_persona.cve_persona)
            data = {
                "nombre": persona.nombre,
                "apellido_paterno": persona.apellido_paterno,
                "apellido_materno": persona.apellido_materno,
                "nombre_grupo": grupo.nombre,
                "nombre_carrera": carrera.nombre,
                "generacion": generacion.generacion
            }
            return JsonResponse(data)
        except Exception as a:
            print(f"Algo salio mal: {a}")
    return JsonResponse({'error': 'Matricula no proporcionada'}, status=400)