from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=150)
    fecha_registro = models.DateField(auto_now_add=True) #Auto_now_add Se colocara la fecha cuando se cree el elemento

    def __str__(self):
        return self.nombre
        
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT, blank=False, null=False) #Con el modo Restrict evitamos el borrado
    nombre = models.CharField(max_length=150,verbose_name='Producto',blank=False,null=False)
    descripcion = models.TextField(null=True,blank=True)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    fecha_registro = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='productos/',blank=True)

    def __str__(self):
        return self.nombre


SEXO = (
    ('Masculino','Masculino'),
    ('Femenino','Femenino'),
)

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=150, null=True)
    apellidos = models.CharField(max_length=150, null=True)
    dni = models.CharField(max_length=8)
    sexo = models.CharField(choices=SEXO , max_length=50, default='Masculino')
    email = models.EmailField(max_length=150, null=True)
    tel = models.CharField(max_length=20)
    fecha_nac = models.DateField(null=True)
    direccion = models.TextField()

    def __str__(self):
        return self.dni
    
ESTADO = (
    ('Solicitado','Solicitado'),
    ('Pagado','Pagado'),
)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.RESTRICT)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    nro_pedido = models.CharField(max_length=50,null=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(choices=ESTADO, max_length=50, null=False, blank=False, default='Solicitado', verbose_name='Estado')

    def __str__(self):
        return self.nro_pedido


class Pedido_Detalle(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete=models.RESTRICT )
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    cantidad = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.producto.nombre