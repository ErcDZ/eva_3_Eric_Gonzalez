from django.db import models

# Create your models here.
class Editoriale(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Comic(models.Model):
    titulo = models.CharField(max_length=250, unique=True)
    portada = models.ImageField(upload_to='portada/', blank=True, null=True)
    fecha_lanzamiento = models.DateField(blank=True, null=True)
    precio = models.PositiveIntegerField()
    numero_tomo = models.PositiveSmallIntegerField()
    tapa_dura = models.BooleanField(default=False)
    stock = models.PositiveIntegerField()
    disponible = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class Reserva(models.Model):
    titulo_identificador = models.CharField(max_length=200, unique=True)
    codigo_reserva = models.PositiveIntegerField(unique=True)
    nombre_comic = models.CharField()
    correo = models.EmailField(unique=True)
    rut = models.PositiveIntegerField(unique=True)
    cantidad_ejemplares = models.PositiveIntegerField()
    fecha_reserva = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.codigo_reserva
