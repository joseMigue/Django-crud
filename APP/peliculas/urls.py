from django.urls import path
from .views import PeliculaCreateView, PeliculaListView,PeliculaDetailView,PeliculaDeleteView,PeliculaUpdateView,UsuarioCreateView,Login
app_name = 'pelicula'
urlpatterns = [
    path('', PeliculaCreateView.as_view(), name="crear"),
    path('lista/', PeliculaListView.as_view(), name='lista'),
    path('detalle/<int:pk>', PeliculaDetailView.as_view(), name="detalle"),
    path('eliminar/<int:pk>', PeliculaDeleteView.as_view(), name='eliminar'),
    path('editar/<int:pk>', PeliculaUpdateView.as_view(), name="editar"),
    path('registrar/',UsuarioCreateView.as_view(), name="registrar"),
    path('login/', Login.as_view(), name='login'),
]