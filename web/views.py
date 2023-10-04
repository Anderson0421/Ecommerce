from django.shortcuts import render
from .models import *

def index(request):
    productos = Producto.objects.all() #Esto nos retorna todos los productos
    categoria = Categoria.objects.all()
    context = {
        'productos':productos,
        'categorias':categoria
    }
    return render(request, 'index.html', context)
    
def FiltroProductos(request, categoria_id):
    """Vista para filtrar productos por categoria"""
    objCategoria = Categoria.objects.get(pk=categoria_id) #Aqui se hace la consulta 
    listaProductos = objCategoria.producto_set.all() #Con esto mostramos los datos
    listaCategorias = Categoria.objects.all() #Y con esto solo mostramos la categorias otra
    
    context = {
        'categorias':listaCategorias,
        'productos':listaProductos,
        'objCategoria':objCategoria
        
    }
    return render(request,'index.html',context)