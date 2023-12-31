# Generated by Django 3.0.7 on 2023-11-24 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicaciones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuestacuestionario',
            name='pregunta_9',
        ),
        migrations.AddField(
            model_name='respuestacuestionario',
            name='pregunta_2',
            field=models.IntegerField(choices=[(1, 'Me gustaría hablar sobre cómo nos ven las personas.'), (2, 'Estoy interesado/a en aprender sobre cómo mantenerme seguro/a en línea.'), (3, 'Me gustaría conocer recursos para personas con discapacidades.'), (4, 'Me interesa explorar temas de género y orientación sexual.'), (5, 'Me gustaría aprender sobre discriminación racial.'), (6, 'Me gustaría conocer formas de superar la discriminación.')], default=2, verbose_name='De las opciones que seleccionaste en la pregunta anterior, ¿cuál te interesa más en este momento?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respuestacuestionario',
            name='pregunta_3',
            field=models.IntegerField(choices=[(1, 'Experiencias de discriminación por apariencia física.'), (2, 'Experiencias de discriminación en línea o ciberacoso.'), (3, 'Experiencias de discriminación debido a una discapacidad.'), (4, 'Experiencias de discriminación de género u orientación sexual.'), (5, 'Experiencias de discriminación racial.'), (6, 'Experiencias de discriminación en el lugar de trabajo o la educación.')], default=3, verbose_name='¿Has tenido experiencias personales relacionadas con alguna de las siguientes categorías?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respuestacuestionario',
            name='pregunta_4',
            field=models.CharField(choices=[('Sí, he buscado recursos y apoyo.', 'Sí, he buscado recursos y apoyo.'), ('No, no he buscado recursos ni apoyo.', 'No, no he buscado recursos ni apoyo.')], default=0, max_length=50, verbose_name='¿Has buscado recursos o apoyo relacionados con estas experiencias?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respuestacuestionario',
            name='pregunta_5',
            field=models.CharField(choices=[('Sí, me gustaría recibir recomendaciones de contenido relacionado con mis intereses.', 'Sí, me gustaría recibir recomendaciones de contenido relacionado con mis intereses.'), ('No, no estoy interesado/a en recibir recomendaciones de contenido.', 'No, no estoy interesado/a en recibir recomendaciones de contenido.')], default=0, max_length=100, verbose_name='¿Te gustaría recibir recomendaciones de contenido específico basado en tus respuestas anteriores?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respuestacuestionario',
            name='pregunta_6',
            field=models.CharField(choices=[('Sí, me gustaría unirme a una comunidad en línea.', 'Sí, me gustaría unirme a una comunidad en línea.'), ('No, no estoy interesado/a en unirme a una comunidad en línea.', 'No, no estoy interesado/a en unirme a una comunidad en línea.')], default=0, max_length=100, verbose_name='¿Te gustaría unirte a una comunidad en línea donde puedas compartir tus experiencias y consejos relacionados con la discriminación?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respuestacuestionario',
            name='pregunta_7',
            field=models.CharField(choices=[('menor', 'Menor a 18 años'), ('18-24', '18 a 24'), ('mayor', '24 o más')], default=0, max_length=50, verbose_name='¿Cuál es tu edad?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='respuestacuestionario',
            name='pregunta_8',
            field=models.CharField(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro'), ('no_responde', 'Prefiero no responder')], max_length=50, verbose_name='¿Cuál es tu género?'),
        ),
    ]
