from django.urls import path
from .views import PerfilDetailView,FavoritosListView,FavoritosAgregar,FavoritosEliminar,PeliculaCreateView, PeliculaListView,PeliculaDetailView,PeliculaDeleteView,PeliculaUpdateView, PerfilView

app_name = 'pelicula'
urlpatterns = [
    path('crear/', PeliculaCreateView.as_view(), name="crear"),
    path('lista/', PeliculaListView.as_view(), name='lista'),
    path('detalle/<int:pk>/', PeliculaDetailView.as_view(), name="detalle"),
    path('eliminar/<int:pk>/', PeliculaDeleteView.as_view(), name='eliminar'),
    path('editar/<int:pk>/', PeliculaUpdateView.as_view(), name="editar"),
    path('agregar_favorito/<int:pk>/', FavoritosAgregar.as_view(), name='agregar_favorito'),
    path('favoritos/',FavoritosListView.as_view(), name='favoritos'),
    path('eliminar_favorito/<int:pk>/', FavoritosEliminar.as_view(), name='eliminar_favorito'),


    path('perfil/<int:pk>/', PerfilView.as_view(), name="perfil"),
    path('editar_perfil/<int:pk>/', PerfilDetailView.as_view(), name="editar_perfil")
]