from django.db import models

class Cuestionario(models.Model):
    pregunta_1 = models.IntegerField(
        verbose_name="¿Te gustaría compartir tus experiencias y obtener recursos relacionados con temas importantes?",
        choices=[
            (1, "Sí, me gustaría hablar sobre cómo nos ven las personas."),
            (2, "Sí, me gustaría aprender sobre cómo mantenerme seguro/a en línea."),
            (3, "Sí, me gustaría conocer recursos para personas con discapacidades."),
            (4, "Sí, me gustaría explorar temas de género y orientación sexual."),
            (5, "Sí, me gustaría aprender sobre discriminación racial."),
            (6, "Sí, me gustaría conocer formas de superar la discriminación."),
        ]
    )

    pregunta_2 = models.IntegerField(
        verbose_name="De las opciones que seleccionaste en la pregunta anterior, ¿cuál te interesa más en este momento?",
        choices=[
            (1, "Me gustaría hablar sobre cómo nos ven las personas."),
            (2, "Estoy interesado/a en aprender sobre cómo mantenerme seguro/a en línea."),
            (3, "Me gustaría conocer recursos para personas con discapacidades."),
            (4, "Me interesa explorar temas de género y orientación sexual."),
            (5, "Me gustaría aprender sobre discriminación racial."),
            (6, "Me gustaría conocer formas de superar la discriminación."),
        ]
    )

    pregunta_3 = models.IntegerField(
        verbose_name="¿Has tenido experiencias personales relacionadas con alguna de las siguientes categorías?",
        choices=[
            (1, "Experiencias de discriminación por apariencia física."),
            (2, "Experiencias de discriminación en línea o ciberacoso."),
            (3, "Experiencias de discriminación debido a una discapacidad."),
            (4, "Experiencias de discriminación de género u orientación sexual."),
            (5, "Experiencias de discriminación racial."),
            (6, "Experiencias de discriminación en el lugar de trabajo o la educación."),
        ]
    )

    pregunta_4 = models.CharField(
        verbose_name="¿Has buscado recursos o apoyo relacionados con estas experiencias?",
        max_length=50,
        choices=[
            ("Sí, he buscado recursos y apoyo.", "Sí, he buscado recursos y apoyo."),
            ("No, no he buscado recursos ni apoyo.", "No, no he buscado recursos ni apoyo."),
        ]
    )

    pregunta_5 = models.CharField(
        verbose_name="¿Te gustaría recibir recomendaciones de contenido específico basado en tus respuestas anteriores?",
        max_length=100,
        choices=[
            ("Sí, me gustaría recibir recomendaciones de contenido relacionado con mis intereses.", "Sí, me gustaría recibir recomendaciones de contenido relacionado con mis intereses."),
            ("No, no estoy interesado/a en recibir recomendaciones de contenido.", "No, no estoy interesado/a en recibir recomendaciones de contenido."),
        ]
    )

    pregunta_6 = models.CharField(
        verbose_name="¿Te gustaría unirte a una comunidad en línea donde puedas compartir tus experiencias y consejos relacionados con la discriminación?",
        max_length=100,
        choices=[
            ("Sí, me gustaría unirme a una comunidad en línea.", "Sí, me gustaría unirme a una comunidad en línea."),
            ("No, no estoy interesado/a en unirme a una comunidad en línea.", "No, no estoy interesado/a en unirme a una comunidad en línea."),
        ]
    )

    pregunta_7 = models.TextField(
        verbose_name="¿Tienes alguna sugerencia o comentario adicional que te gustaría compartir con nosotros?",
        blank=True,
    )

    pregunta_8 = models.CharField(
        verbose_name="¿Cuál es tu edad?",
        max_length=50,
        choices=[
            ("menor", "Menor a 18 años"),
            ("18-24", "18 a 24"),
            ("mayor", "24 o más"),
        ]
    )

    pregunta_9 = models.CharField(
        verbose_name="¿Cuál es tu género?",
        max_length=50,
        choices=[
            ("masculino", "Masculino"),
            ("femenino", "Femenino"),
            ("otro", "Otro"),
            ("no_responde", "Prefiero no responder"),
        ]
    )

    puntaje_total = models.IntegerField(null=True, blank=True)
    categoria = models.CharField(max_length=50, null=True, blank=True)

    def calcular_puntaje_y_categoria(self):
        puntaje = self.pregunta_1 + self.pregunta_2 + self.pregunta_3
        self.puntaje_total = puntaje

        if puntaje >= 10:
            self.categoria = "Discriminación por Género y Orientación Sexual"
        elif puntaje >= 7:
            self.categoria = "Discriminación por Discapacidad"
        elif puntaje >= 4:
            self.categoria = "Discriminación Digital y Ciberacoso"
        else:
            self.categoria = "Discriminación por Apariencia Física"

