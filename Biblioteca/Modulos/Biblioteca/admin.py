from django.contrib import admin

from Modulos.Biblioteca.models import Autores, Categorias, Editoriales, Libros

# Register your models here.
admin.site.register(Autores)
admin.site.register(Categorias)
admin.site.register(Editoriales)
admin.site.register(Libros)
