from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView,DetailView
from .models import Pelicula, Usuario, Genero, Comentario
from django.urls import reverse_lazy
from .forms import PeliculaForm
from django.forms import forms

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


    
