from django.db import models

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

