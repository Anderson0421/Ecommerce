from typing import Any
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.views.generic import ListView, DetailView
from .carrito import Cart

"""De esta forma seria con vista Generica"""
class index_view(ListView):
    model = Producto
    template_name = 'index.html'
    context_object_name = 'productos'
    # queryset = Producto.objects.all()

    def get_context_data(self,*args ,**kwargs):
        context = super().get_context_data(*args ,**kwargs)
        context['productTotal'] = Producto.objects.all()
        context['categorias'] = Categoria.objects.all()
        return context


class Filtro_Productos(DetailView):
    model = Categoria
    template_name = 'index.html'
    context_object_name = 'categoria'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = self.object.producto_set.all()
        context['productTotal'] = Producto.objects.all()
        context['categorias'] = Categoria.objects.all()
        return context

def Search_Producto(request):
    nombre = request.POST['nombre'].capitalize()
    listaProducto = Producto.objects.filter(nombre__contains=nombre)
    listaCategoria = Categoria.objects.all()

    context={
        'categorias':listaCategoria,
        'productos':listaProducto
    }
    return render(request, 'index.html',context)

 
class Product_Detail(DetailView):
    model = Producto
    template_name ='producto.html'
    context_object_name = 'productos'

    def get_object(self, queryset=None):
       # Obtiene el objeto Producto o retorna un error 404 si no existe 
        return get_object_or_404(Producto, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context


#Vistas para el carrito de compras

def Carrito_View(request):
    return render(request,'carrito.html')


def Add_Carrito(request,producto_id):
    if request.method == 'POST':
        cantidad = int(request.POST['cantidad'])
    else:
        cantidad = 1

    objProducto = Producto.objects.get(pk=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,cantidad)
    if request.method == 'GET': #GOOOOOOOOOOOOOOOOOOOOOOOOOOD
        return redirect('/') #GOOOOOOOOOOOOOOOOOOOOOOOOOOD


    return render(request,'carrito.html')

def Del_Carrito(request,producto_id):
    objProducto = Producto.objects.get(pk=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.delete(objProducto)

    return render(request,'carrito.html')


def Clear_Carrito(request):
    carrito = Cart(request)
    carrito.clear()
    return render(request, 'carrito.html')