from django.contrib import admin
from .models import Categoria,Producto


@admin.register(Categoria)
class AdminCategoria(admin.ModelAdmin):
    list_display= ('nombre','fecha_registro')
    search_fields =('nombre',)
    list_filter = ('nombre',)

admin.site.register(Producto)