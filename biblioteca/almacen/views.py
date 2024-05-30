from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import acervo_model
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index_acervo(request):
        listado = acervo_model.objects.all()
        return render(request, 'index_almacen.html', { "list_acervo": listado})

def acervo_registro(request):
        try:
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
                    titulo = titulo,
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
            messages.success(request, 'Registro agregado')
            return redirect('acervo')
        except:
            messages.error(request, '¡Algo salio mal!')
            return redirect('acervo')

def delete_acervo(request, colocacion):
        acervo_delete = acervo_model.objects.get(colocacion=colocacion)
        acervo_delete.delete()
        messages.success(request, 'Registro Eliminado')
        return redirect(to="acervo")
        # return redirect('acervo/')