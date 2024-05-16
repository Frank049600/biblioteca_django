from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import acervo_model
from datetime import datetime

# Create your views here.
def index_acervo(request):
        listado = acervo_model.objects.all()
        return render(request, 'index_almacen.html', { "list_acervo": listado})

def acervo_registro(request):
        titulo = request.POST['title']
        autor = request.POST['autor']
        editorial = request.POST['edito']
        cant = request.POST['cant']
        colocacion = request.POST['coloca']
        edicion = request.POST['edic']
        año = request.POST['anio']
        type_adqui = request.POST['typeAdq']
        estado = request.POST['stateBook']
        fechaRegistro = datetime.now()

        acervo = acervo_model.objects.create(
                 
                autor = autor,
                editorial = editorial,
                cant = cant,
                colocacion = colocacion,
                edicion = edicion,
                año = año,
                type_adqui = type_adqui,
                estado = estado,
                fechaRegistro = fechaRegistro
        )
        return redirect('')

# def deleteAcervo(request, codigo):
#         acervo_delete = acervo_model.objects.get(codigo=codigo)
#         acervo_delete.delete()
#         return redirect('acervo/')
