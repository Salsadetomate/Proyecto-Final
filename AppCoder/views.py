from django.shortcuts import render
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import CursoFormulario, ProfesorFormulario, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required



def curso(request):

      curso =  Economia(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")



def economia(request):

    return render(request, "AppCoder/economia.html")


def sobremi(request):

      return render(request, "AppCoder/sobremi.html")

def administracion(request):

      return render(request, "AppCoder/administracion.html")

def finanzas(request):

      return render(request, "AppCoder/finanzas.html")

def cart(request):
    return render(request, "AppCoder/cart.html")


def profesores(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:  

                  informacion = miFormulario.cleaned_data

                  profesor = Finanzas (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") 

      else: 

            miFormulario= ProfesorFormulario() 

      return render(request, "AppCoder/finanzas.html", {"miFormulario":miFormulario})


def profesoress(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:  

                  informacion = miFormulario.cleaned_data

                  profesor = Administracion (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") 

      else: 

            miFormulario= ProfesorFormulario() 

      return render(request, "AppCoder/administracion.html", {"miFormulario":miFormulario})






def buscar(request):



    if  request.GET["camada"]:

	      
        camada = request.GET['camada'] 
        cursos = Economia.objects.filter(camada__icontains=camada)

        return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})

    else:
        
        respuesta="No enviaste Datos"

    return HttpResponse(respuesta)



def leerProfesores(request):

      profesores = Finanzas.objects.all() 

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)


def eliminarProfesor(request, profesor_nombre):

    profesor = Finanzas.objects.get(nombre=profesor_nombre)
    profesor.delete()

    profesores = Finanzas.objects.all()  

    contexto = {"profesores": profesores}

    return render(request, "AppCoder/leerProfesores.html", contexto)

def editarProfesor(request, profesor_nombre):

    
    profesor = Finanzas.objects.get(nombre=profesor_nombre)

    
    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  

            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']

            profesor.save()

      
            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido,
                                                   'email': profesor.email, 'profesion': profesor.profesion})


    return render(request, "AppCoder/editarProfesor.html", {"miFormulario": miFormulario, "profesor_nombre": profesor_nombre})



class CursoList(ListView):

    model = Economia
    template_name = "AppCoder/cursos_list.html"

class CursoDetalle(DetailView):

    model = Economia
    template_name = "AppCoder/curso_detalle.html"

class CursoCreacion(CreateView):

    model = Economia
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'camada']

class CursoUpdate(UpdateView):

    model = Economia
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'camada']

class CursoDelete(DeleteView):

    model = Economia
    success_url = "/AppCoder/curso/list"



def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form})


def register(request):

      if request.method == 'POST':

            form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})


@login_required
def inicio(request):

    return render(request, "AppCoder/inicio.html")
