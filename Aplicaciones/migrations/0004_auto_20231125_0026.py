# Generated by Django 3.0.7 on 2023-11-25 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicaciones', '0003_auto_20231125_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestacuestionario',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicaciones.Categoria'),
        ),
    ]
