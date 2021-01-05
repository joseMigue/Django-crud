from .models import Pelicula
from django.forms import ModelForm

class PeliculaForm(ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'