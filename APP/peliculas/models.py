from django.db import models
from django.contrib.auth.models import User, Permission
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    nombre = models.CharField(max_length=50,unique=True)
    direccion = models.CharField(max_length=50)
    genero = models.ManyToManyField(Genero)
    fecha_estreno = models.DateField(auto_now_add=True)
    sinopsis = models.TextField()

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_de_nacimiento = models.DateField(auto_now=False,auto_now_add=True)
    favoritos = models.ManyToManyField(Pelicula)
    bloqueado = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario.username

    def agregar_favorito(self,pelicula):
        self.favoritos.add(pelicula)
        
    def eliminar_favorito(self,pelicula):
        self.favoritos.remove(pelicula)

@receiver(post_save, sender= User)
def crear_usuario(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Usuario(usuario=user)
        user_profile.save()
        user.user_permissions.add(Permission.objects.get(name='Can view pelicula'))
post_save.connect(crear_usuario, sender=User)  

class Comentario(models.Model):
    texto = models.CharField(max_length=255)
    fecha = models.DateField(auto_now=False,auto_now_add=True)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return 'comentario de '+ self.usuario.usuario.username