from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context


def saludo(request):
    return HttpResponse("oni oni")


def probandotemplate(self):
    #miHtml=open(r"C:\Users\marco\Documents\Programación\CoderHouse\Preentrega3\PythonProyecto1\Proyecto1\Proyecto1\Plantillas\template1.html")
    
    nom= "Marcos"
    ap= "Arrut"

    diccionario= {"nombre": nom, "apellido": ap}

    plantilla= loader.get_template("plantilla1.html")

    Documento = plantilla.render(diccionario)

    return HttpResponse(Documento)

