from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    disponibilidad = models.IntegerField()

    def __str__(self):
        return self.nombre


class Usuario(AbstractUser):
    rut = models.CharField(max_length=12, unique=True,
                           error_messages={'unique': "Un usuario con el mismo rut ya existe."})
    username = models.CharField(max_length=12, blank=True)
    email = models.EmailField(unique=True, error_messages={'unique': "Un usuario con el mismo rut ya existe."})
    fechaRegistro = models.DateTimeField(default=timezone.now)
    razonSocial = models.CharField(max_length=100, blank=True)
    esSocio = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    total = models.IntegerField(default=0)

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'email']

    @property
    def is_admin(self):
        if self.is_staff:
            return True

    def __str__(self):
        return self.get_username() + " - " + self.get_full_name()


class Registro(models.Model):

    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    socioAportador = models.CharField(max_length=100, blank=True)
    cliente = models.CharField(max_length=100, blank=True)
    fechaAporte = models.DateTimeField(default=timezone.now)

    def __str__(self):
        string = self.producto + " / "
        if self.socioAportador == "":
            string += "No hay socio asignado"
        else:
            string += self.socioAportador
        string += " / "
        string += str(self.fechaAporte)
        return string
