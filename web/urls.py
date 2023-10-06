from django.urls import path
from .views import *
app_name = 'web'

urlpatterns = [
    path('', index_view.as_view(), name='index'),
    path('category/<int:pk>', Filtro_Productos.as_view(), name='filtrado'),
    path('productos/', Search_Producto, name='filter'),
    path('producto/detail/<int:pk>', Product_Detail.as_view(), name='details'),
    path('carrito/', Carrito_View, name='carrito'),
    path('carrito/add/<int:producto_id>',Add_Carrito,name='add_carrito'),
    path('carrito/delete/<int:producto_id>',Del_Carrito,name='del_carrito'),
    path('carrito/clear/',Clear_Carrito,name='clear_carrito'),
]
