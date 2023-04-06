
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota,view responsável, nome de referência
    # usuarios.com
    path('', views.home, name='home'),  # link das paginas
    # usuario.com/usuarios
    path('usuarios/', views.users, name='listagem_usuarios')
]
