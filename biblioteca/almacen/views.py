from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index_acervo(request):
        return render(request, 'index_almacen.html')

