from django.shortcuts import render
from django.views.generic.edit import DeleteView
from .models import User


def home(request):  # REQUEST: permite acessar os dados presente naquela pagina
    return render(request, 'usuarios/home.html')  # criar a pagina no view


def users(request):
    # Salvar os dados da tela para o banco de daods.
    new_user = User()
    new_user.username = request.POST.get('username')
    new_user.email = request.POST.get('email')
    new_user.save()
    # Exibir todos os usuários já cadastrados
    users = {
        'users': User.objects.all()
    }

    # retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', users)


def delete_all_users():
    delete_user = User.objects.all()
    delete_user.delete()


# delete_user()''
