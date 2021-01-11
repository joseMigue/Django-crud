from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.views.generic.base import RedirectView
from .models import Pelicula, Usuario, Genero, Comentario
from django.urls import reverse_lazy
from .forms import PeliculaForm, UsuarioForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Permission
# Create your views here.


class PeliculaCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Pelicula
    form_class = PeliculaForm
    permission_required = 'peliculas.add_pelicula'
    template_name = "pelicula/pelicula_form.html"
    success_url = reverse_lazy('pelicula:lista')

class PeliculaListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Pelicula
    permission_required = 'peliculas.view_pelicula'
    template_name = "pelicula/pelicula_lista.html"

class PeliculaDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Pelicula
    permission_required = 'peliculas.view_pelicula'
    template_name = "pelicula/pelicula_detalle.html"

class PeliculaDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Pelicula
    success_url = reverse_lazy('pelicula:lista')
    permission_required = 'peliculas.delete_pelicula'

class PeliculaUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    permission_required = 'peliculas.change_pelicula'
    template_name = "pelicula/pelicula_form.html"
    success_url = reverse_lazy('pelicula:lista')

class FavoritosAgregar(LoginRequiredMixin,RedirectView):
    pattern_name = 'pelicula:detalle'
    def get_redirect_url(self,*args,**kwargs):
        peli = get_object_or_404(Pelicula,pk=kwargs['pk'])
        self.request.user.usuario.agregar_favorito(peli)
        return super().get_redirect_url(**kwargs) 

class FavoritosEliminar(LoginRequiredMixin,RedirectView): 
    permanent =False
    query_string = True
    pattern_name = 'pelicula:lista'
    def get_redirect_url(self,*args,**kwargs):
        peli = get_object_or_404(Pelicula,pk=kwargs['pk'])
        #self.request.user.usuario.favoritos.remove(peli)
        self.request.user.usuario.eliminar_favorito(peli)
        return super().get_redirect_url()

class FavoritosListView(LoginRequiredMixin,ListView):
    model = Pelicula
    template_name = "pelicula/pelicula_lista.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.request.user.usuario.favoritos.all()
        return context
                                                            
class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "usuario/usuario_form.html"
    success_url = reverse_lazy('pelicula:lista')


class Login(LoginView):
    redirect_authenticated_user = 'pelicula:lista'
    template_name = "usuario/usuario_login.html"
