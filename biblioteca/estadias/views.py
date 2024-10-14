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
from static.context_processors import group_permission
from django.http import JsonResponse
import base64

# Create your views here.
# def modal_registro(request):
#     return render(request, 'modal_registro.html')
def get_fullname_grupo(request):
    user = request.user
    cve = Usuario.objects.get(login=user)
    persona = Persona.objects.get(cve_persona=cve.cve_persona)
    group = group_permission(request, True)
    name = persona.nombre + ' ' + persona.apellido_paterno + ' ' + persona.apellido_materno

    return {
        "group": group,
        "name": name
    }

def index_proyectos(request):
    form = estadias_form()
    fullname = get_fullname_grupo(request)['name']
    flag = True
    if get_fullname_grupo(request)['group'] == '27 Docentes':
        flag = False

    reporte = model_estadias.objects.all() if flag else model_estadias.objects.filter(asesor_academico=fullname)
    side_code = 300
    return render(request,'index_proyectos.html',{"reporte":reporte, "form":form,"side_code":side_code})

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
            name_ref = file_new_name(alumno, form.cleaned_data['reporte_file'].name)

            # Archivo reporte
            # fs = FileSystemStorage()
            # response_file = fs.save(name_ref, form.cleaned_data['reporte_file'])

            # Llamado de función para convertir documento a base64
            base64 = convert_base64(form.cleaned_data['reporte_file'])

            proyectos=model_estadias.objects.create(
                    proyecto = proyecto,
                    matricula = matricula,
                    alumno = alumno,
                    asesor_academico = asesor_academico,
                    generacion = generacion,
                    empresa = empresa,
                    asesor_orga = asesor_orga,
                    carrera = carrera,
                    reporte = name_ref,
                    base64 = base64
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

# Función para convertir documento a base64
def convert_base64(doc, name_doc = False, revert = False, data = False):
    # Se convierte el pdf en formato base64
    if not revert:
        # Lee el documento que llega en formulario
        file = doc.read()
        # Convierte el documento en base64
        encoded_string = base64.b64encode(file)

        return encoded_string.decode('utf-8')
    else:
        bytes = base64.b64decode(data, validate = True)
        if bytes[0:4] != b'%PDF':
            raise ValueError('False de firma del archivo PDF')
        # Se escribe el contenido del PDF en un archivo local
        f = open('file_convert.pdf', 'wb')
        f.write(bytes)
        f.close()

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