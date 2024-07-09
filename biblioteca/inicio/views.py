from django.shortcuts import render, redirect
from static.utils import dd
from almacen.models import acervo_model

# Create your views here.
def index_inicio(request):
    side_code = 100
    datos = acervo_model.objects.all()
    total_book = 0
    format_libro = 0
    format_disco = 0
    for cant in datos:
        if cant.formato == 'Libro':
            format_libro += 1
        if cant.formato == 'Disco':
            format_disco += 1
        total_book += cant.cant
    # Obtener el total por estados
    states = []
    EXC = 0
    BUE = 0
    REG = 0
    MAL = 0
    for state in datos:
        if state.estado == 'Excelente':
            EXC += 1
        if state.estado == 'Bueno':
            BUE += 1
        if state.estado == 'Regular':
            REG += 1
        if state.estado == 'Malo':
            MAL += 1
    # Se almacenan para el uso de al gráfica
    states.append([EXC,BUE,REG,MAL])
    # Suma total de estados (diferente a la suma de todos los libros)
    total_state = states[0][0] + states[0][1] + states[0][2]
    return render(request, 'index_inicio.html', { "total_book": total_book, "states": states[0], "total_state": total_state, "side_code":side_code, "cant_libros":format_libro, "cant_discos": format_disco })