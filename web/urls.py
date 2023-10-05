from django.urls import path
from .views import *
app_name = 'web'

urlpatterns = [
    path('', index_view.as_view(), name='index'),
    path('category/<int:pk>', Filtro_Productos.as_view(), name='filtrado'),
    path('productos/', Search_Producto, name='filter'),
    path('producto/detail/<int:pk>', Product_Detail.as_view(), name='details')
]
