from contextlib import redirect_stderr
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.shortcuts import render, redirect
from BaseDatos.models import Productos
import random


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

def crud(request):
  productos = Productos.objects.all()
  contexto = {'productos':productos}
  return render(request,"crud.html",contexto)

def login(request):
  return render(request,"login.html")

def eliminarProducto(request,codigo):
  productos = Productos.objects.get(codigo=codigo)
  productos.delete()
  return redirect('/crud/')

def crearProducto(request):
  Productos.objects.create(codigo=random.randint(7, 45),
                          nombre="objeto random",
                          descripcion="descripcion random",
                          disponible = 1,
                          fechaIncorporacion = "2022-02-02",
                          correoProveedor = "pablekereke@adsfa.cl"
                               )

  return redirect('/crud/')

def resultado(request):
  mensaje = f'se ha logeado el usuario {request.GET["correo"]}'
  productos = Productos.objects.filter(nombre__icontains="pelota")
  contexto = {'mensaje':mensaje,'productos':productos}
  return render(request,"resultado.html",contexto)