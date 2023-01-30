from django.shortcuts import render
from django.http import HttpResponse
from AppCoder import *

from .models import *

#PONER UN IMPORT FORMSSSS

def Introduccion(request):
    return render(request, "AppCoder/Introduccion.html")

def sobremi(request):
    return render(request, "AppCoder/sobremi.html")




