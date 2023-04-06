from django.db import models


class User(models.Model):

    # irá gerar um número sequencial, porém não duplicável para representar o usuário.
    id_user = models.AutoField(primary_key=True)
    username = models.TextField(max_length=255)
    email = models.TextField(max_length=100)
