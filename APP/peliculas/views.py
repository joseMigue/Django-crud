from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView,DetailView
from .models import Pelicula, Usuario, Genero, Comentario
from django.urls import reverse_lazy
from .forms import PeliculaForm, UsuarioForm,User
from django.forms import forms
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

# Create your views here.
class PeliculaCreateView(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model = Pelicula
    form_class = PeliculaForm
    permission_required = 'peliculas.add_pelicula'
    template_name = "pelicula/pelicula_form.html"
    success_url = reverse_lazy('pelicula:lista')

class PeliculaListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model = Pelicula
    permission_required = 'peliculas.view_pelicula'
    template_name = "pelicula/pelicula_lista.html"
    
class PeliculaDetailView(PermissionRequiredMixin,LoginRequiredMixin,DetailView):
    model = Pelicula
    permission_required = 'peliculas.view_pelicula'
    template_name = "pelicula/pelicula_detalle.html"
     
class PeliculaDeleteView(PermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    model = Pelicula
    form_class = PeliculaForm
    success_url = reverse_lazy('pelicula:lista')
    permission_required = 'peliculas.delete_pelicula'

class PeliculaUpdateView(PermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    permission_required = 'peliculas.change_pelicula'
    template_name = "pelicula/pelicula_form.html"
    success_url = reverse_lazy('pelicula:lista')
    
class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "usuario/usuario_form.html"
    success_url = reverse_lazy('pelicula:lista')

class Login(LoginView):
    redirect_authenticated_user = 'pelicula:lista'
    template_name ="usuario/usuario_login.html"
