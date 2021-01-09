from django.urls import path
from .views import FavoritosListView,FavoritosAgregar,FavoritosEliminar,PeliculaCreateView, PeliculaListView,PeliculaDetailView,PeliculaDeleteView,PeliculaUpdateView

app_name = 'pelicula'
urlpatterns = [
    path('crear/', PeliculaCreateView.as_view(), name="crear"),
    path('lista/', PeliculaListView.as_view(), name='lista'),
    path('detalle/<int:pk>/', PeliculaDetailView.as_view(), name="detalle"),
    path('eliminar/<int:pk>/', PeliculaDeleteView.as_view(), name='eliminar'),
    path('editar/<int:pk>/', PeliculaUpdateView.as_view(), name="editar"),
    path('agregarFavorito/<int:pk>/', FavoritosAgregar.as_view(), name='agregar_favorito'),
    path('favoritos/',FavoritosListView.as_view(), name='favoritos'),
    path('fav/<int:pk>/', FavoritosEliminar.as_view(), name='eliminar_favorito'),
]