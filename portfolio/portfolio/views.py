from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.shortcuts import render
from BaseDatos.models import Productos

def saludo(request):
  
  doc_externo=open("static/index.html")
  plt=Template(doc_externo.read())
  doc_externo.close()
  ctx = Context()
  documento=plt.render(ctx)
  return HttpResponse(documento)

def productos(request):
  productos=[
    {
      "url":"https://sodimac.scene7.com/is/image/SodimacCL/8758581?fmt=jpg&fit=fit,1&wid=160&hei=160",
      "descripcion": "una cama"
    }
]
  doc_externo=open("static/productos.html")
  plt=Template(doc_externo.read())
  doc_externo.close()
  ctx = Context({"nombre":"pableteeee","lista":["elemento1","elemento2","elemento3"]})
  documento=plt.render(ctx)
  return HttpResponse(documento)


def login(request):
  return render(request,"login.html")

def resultado(request):
  mensaje = f'se ha logeado el usuario {request.GET["correo"]}'
  productos = Productos.objects.filter(nombre__icontains="pelota")
  contexto = {'mensaje':mensaje,'productos':productos}
  return render(request,"resultado.html",contexto)