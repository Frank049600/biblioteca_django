from django.shortcuts import render

# Create your views here.
def modal_registro(request):
        return render(request, 'modal_registro.html')

def index_proyectos (request):
        return render(request,'tablaformulario.html')

