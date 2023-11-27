# Generated by Django 3.0.7 on 2023-11-25 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicaciones', '0004_auto_20231125_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='categoria',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='_usuario_groups_+', related_query_name='usuario_group', to='Aplicaciones.Usuario', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='_usuario_user_permissions_+', related_query_name='usuario_permission', to='Aplicaciones.Usuario', verbose_name='user permissions'),
        ),
    ]