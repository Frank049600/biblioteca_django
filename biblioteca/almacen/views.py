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
<<<<<<< HEAD
                titulo = titulo,
=======

                 

                titulo = titulo,

>>>>>>> 1254151e71b63e74d9f2cedf6fbe5544ac2f36ff
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
<<<<<<< HEAD
        # return redirect('')
        return redirect('acervo')
=======

        return redirect('')

        return redirect('acervo/')

>>>>>>> 1254151e71b63e74d9f2cedf6fbe5544ac2f36ff

def delete_acervo(request, colocacion):
        acervo_delete = acervo_model.objects.get(colocacion=colocacion)
        acervo_delete.delete()
        messages.success(request, 'Registro Eliminado')
        return redirect(to="acervo")
        # return redirect('acervo/')
