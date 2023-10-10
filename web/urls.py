from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
app_name = 'web'

urlpatterns = [
    path('', views.index,name='index'),
    #Productos
    path('Productos/Categoria/<int:categoria_id>',views.Producto_Categoria,name='productosPorCategoria'),
    path('Productos/Search/',views.Productos_Nombre,name='productosPorNombre'),
    path('producto/<int:producto_id>',views.Producto_Detalle,name='producto'),

    #Carrito
    path('Carrito',views.carrito,name='carrito'),
    path('Carrito/add/<int:producto_id>',views.Carrito_add,name='agregarCarrito'),
    path('Carrito/del/<int:producto_id>',views.Carrito_del,name='eliminarProductoCarrito'),
    path('Carrito/clear',views.Carrito_clear,name='limpiarCarrito'),

    #Usuarios
    path('Usuario/New/',views.crearUsuario,name='crearUsuario'),
    path('Cuenta/',views.cuentaUsuario,name='cuenta'),
    path('Cliente/Actualizar/',views.actualizarCliente,name='actualizarCliente'),

    #logins
    path('login/',views.ViewLogin.as_view(),name='loginUsuario'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #Pedidos / Compras
    path('Pedido/Register/',views.registrarPedido,name='registrarPedido'),
    
    path('Compra/',views.registrarCompra,name='compra'),
    path('confirmacion/',views.confirmacionPedido,name='confirmacion')
] 
