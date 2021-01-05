from django.contrib import admin
from .models import Comentario,Genero,Pelicula,Usuario
# Register your models here.
admin.site.register(Comentario)
admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(Usuario)