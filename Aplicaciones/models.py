<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import AbstractUser
class Usuario(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True)

    # Agregar related_name para evitar conflictos
=======
# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True)

>>>>>>> 0771c18659a3602f5df4adcb586b93171e4256b4
    groups = models.ManyToManyField(
        'self',
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
<<<<<<< HEAD
        related_name="usuarios",
        related_query_name="user",
=======
        related_name="usuario_groups",  # Cambiado a 'usuario_groups'
        related_query_name="usuario_group",
>>>>>>> 0771c18659a3602f5df4adcb586b93171e4256b4
    )
    user_permissions = models.ManyToManyField(
        'self',
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
<<<<<<< HEAD
        related_name="usuarios",
        related_query_name="user",
    )
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def calcular_puntaje_y_categoria(self):
        puntaje = self.pregunta_1 + self.pregunta_2 + self.pregunta_3
        self.puntaje_total = puntaje
=======
        related_name="usuario_permissions",  # Cambiado a 'usuario_permissions'
        related_query_name="usuario_permission",
    )


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100, blank=True)

    def calcular_puntaje_y_categoria(self, pregunta_1, pregunta_2, pregunta_3):
        puntaje = pregunta_1 + pregunta_2 + pregunta_3
>>>>>>> 0771c18659a3602f5df4adcb586b93171e4256b4

        if puntaje >= 10:
            self.categoria = "Discriminación por Género y Orientación Sexual"
        elif puntaje >= 7:
            self.categoria = "Discriminación por Discapacidad"
        elif puntaje >= 4:
            self.categoria = "Discriminación Digital y Ciberacoso"
        else:
            self.categoria = "Discriminación por Apariencia Física"
    
    def obtener_template_categoria(self):
        if self.categoria == "Discriminación por Género y Orientación Sexual":
            return "template_genero_orientacion.html"
        elif self.categoria == "Discriminación por Discapacidad":
            return "template_discapacidad.html"
        elif self.categoria == "Discriminación Digital y Ciberacoso":
            return "template_digital_ciberacoso.html"
        else:
            return "template_apariencia_fisica.html"
<<<<<<< HEAD

class RespuestaCuestionario(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
=======
        
        

class RespuestaCuestionario(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
>>>>>>> 0771c18659a3602f5df4adcb586b93171e4256b4

    OPCIONES_PREGUNTA1 = [
        (1, "Sí, me gustaría hablar sobre cómo nos ven las personas."),
        (2, "Sí, me gustaría aprender sobre cómo mantenerme seguro/a en línea."),
        (3, "Sí, me gustaría conocer recursos para personas con discapacidades."),
        (4, "Sí, me gustaría explorar temas de género y orientación sexual."),
        (5, "Sí, me gustaría aprender sobre discriminación racial."),
        (6, "Sí, me gustaría conocer formas de superar la discriminación."),
    ]

    OPCIONES_PREGUNTA2 = [
<<<<<<< HEAD

            (1, "Me gustaría hablar sobre cómo nos ven las personas."),
            (2, "Estoy interesado/a en aprender sobre cómo mantenerme seguro/a en línea."),
            (3, "Me gustaría conocer recursos para personas con discapacidades."),
            (4, "Me interesa explorar temas de género y orientación sexual."),
            (5, "Me gustaría aprender sobre discriminación racial."),
            (6, "Me gustaría conocer formas de superar la discriminación."),

    ]
    OPCIONES_PREGUNTA3 = [ 
            (1, "Experiencias de discriminación por apariencia física."),
            (2, "Experiencias de discriminación en línea o ciberacoso."),
            (3, "Experiencias de discriminación debido a una discapacidad."),
            (4, "Experiencias de discriminación de género u orientación sexual."),
            (5, "Experiencias de discriminación racial."),
            (6, "Experiencias de discriminación en el lugar de trabajo o la educación."),
            ]
=======
        (1, "Me gustaría hablar sobre cómo nos ven las personas."),
        (2, "Estoy interesado/a en aprender sobre cómo mantenerme seguro/a en línea."),
        (3, "Me gustaría conocer recursos para personas con discapacidades."),
        (4, "Me interesa explorar temas de género y orientación sexual."),
        (5, "Me gustaría aprender sobre discriminación racial."),
        (6, "Me gustaría conocer formas de superar la discriminación."),
    ]

    OPCIONES_PREGUNTA3 = [ 
        (1, "Experiencias de discriminación por apariencia física."),
        (2, "Experiencias de discriminación en línea o ciberacoso."),
        (3, "Experiencias de discriminación debido a una discapacidad."),
        (4, "Experiencias de discriminación de género u orientación sexual."),
        (5, "Experiencias de discriminación racial."),
        (6, "Experiencias de discriminación en el lugar de trabajo o la educación."),
    ]
>>>>>>> 0771c18659a3602f5df4adcb586b93171e4256b4

    pregunta_1 = models.IntegerField(
        verbose_name="¿Te gustaría compartir tus experiencias y obtener recursos relacionados con temas importantes?",
        choices=OPCIONES_PREGUNTA1
    )

    pregunta_2 = models.IntegerField(
        verbose_name="De las opciones que seleccionaste en la pregunta anterior, ¿cuál te interesa más en este momento?",
        choices=OPCIONES_PREGUNTA2
    )
<<<<<<< HEAD
    default= 3

    pregunta_3 = models.IntegerField(
        verbose_name="¿Has tenido experiencias personales relacionadas con alguna de las siguientes categorías?",
        choices=OPCIONES_PREGUNTA3
           
        
=======
    
    pregunta_3 = models.IntegerField(
        verbose_name="¿Has tenido experiencias personales relacionadas con alguna de las siguientes categorías?",
        choices=OPCIONES_PREGUNTA3
>>>>>>> 0771c18659a3602f5df4adcb586b93171e4256b4
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

    pregunta_7 = models.CharField(
        verbose_name="¿Cuál es tu edad?",
        max_length=50,
        choices=[
            ("menor", "Menor a 18 años"),
            ("18-24", "18 a 24"),
            ("mayor", "24 o más"),
        ]
    )

    pregunta_8 = models.CharField(
        verbose_name="¿Cuál es tu género?",
        max_length=50,
        choices=[
            ("masculino", "Masculino"),
            ("femenino", "Femenino"),
            ("otro", "Otro"),
            ("no_responde", "Prefiero no responder"),
        ]
    )

<<<<<<< HEAD
    puntaje_total = models.IntegerField(null=True, blank=True)
    categoria = models.CharField(max_length=50, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.categoria.calcular_puntaje_y_categoria()
        self.categoria_resultado = self.categoria.obtener_template_categoria()
        super().save(*args, **kwargs)


=======
    def clean(self):
        # Validar que el usuario esté registrado
        if not self.usuario_id:
            raise ValidationError("El usuario debe estar registrado para responder al cuestionario.")

    def save(self, *args, **kwargs):
        if not self.categoria_id:
            categoria_nombre = self.categoria.calcular_puntaje_y_categoria(
                self.pregunta_1, self.pregunta_2, self.pregunta_3
            )
            nueva_categoria, _ = Categoria.objects.get_or_create(nombre=categoria_nombre)
            self.categoria = nueva_categoria

        super().save(*args, **kwargs)

>>>>>>> 0771c18659a3602f5df4adcb586b93171e4256b4
