# Generated by Django 4.2 on 2023-04-05 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0002_rename_usuarios_user_rename_id_usuario_user_id_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.TextField(max_length=100),
        ),
    ]
