from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView,DetailView
from .models import Pelicula, Usuario, Genero, Comentario
from django.urls import reverse_lazy
from .forms import PeliculaForm, UsuarioForm,User
from django.forms import forms
from django.contrib.auth.views import LoginView,LogoutView

# Create your views here.



class PeliculaCreateView(CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = "pelicula/pelicula_form.html"
    success_url = reverse_lazy('pelicula:lista')

class PeliculaListView(ListView):
    model = Pelicula
    template_name = "pelicula/pelicula_lista.html"
    
class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = "pelicula/pelicula_detalle.html"
     
class PeliculaDeleteView(DeleteView):
    model = Pelicula
    form_class = PeliculaForm
    success_url = reverse_lazy('pelicula:lista')

class PeliculaUpdateView(UpdateView):
    model = Pelicula
    form_class = PeliculaForm
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
