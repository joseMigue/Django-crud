from .models import Pelicula, Usuario
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PeliculaForm(ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'

class UsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=10, 
                required=True,
            )

    class Meta:
        model = User
        fields = ('username','password1','password2')
