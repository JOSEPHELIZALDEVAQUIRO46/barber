from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Barberia(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    descripcion = models.TextField()
    imagen_logo = models.ImageField(upload_to='barberias_logos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Barbero(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    barberia = models.ForeignKey(Barberia, on_delete=models.CASCADE)
    certificado_profesional = models.FileField(upload_to='certificados/', null=True, blank=True)
    anos_experiencia = models.IntegerField()
    especialidad = models.CharField(max_length=100)
    disponibilidad = models.TextField()

    def __str__(self):
        return f"{self.usuario.get_full_name()} - {self.barberia.nombre}"

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_estimada = models.DurationField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='servicios/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class CatalogoCortes(models.Model):
    barbero = models.ForeignKey(Barbero, on_delete=models.CASCADE)
    nombre_estilo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='catalogo_cortes/')

    def __str__(self):
        return f"{self.nombre_estilo} - {self.barbero.usuario.get_full_name()}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Contabilidad(models.Model):
    fecha = models.DateField(default=timezone.now)
    ingresos = models.DecimalField(max_digits=10, decimal_places=2)
    gastos = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def beneficio(self):
        return self.ingresos - self.gastos

    def __str__(self):
        return f"Contabilidad - {self.fecha.strftime('%B %Y')}"

class Promociones(models.Model):
    barberia = models.ForeignKey(Barberia, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.ImageField(upload_to='promociones/', null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.barberia.nombre}"
    
class Cita(models.Model):
    nombre_completo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    fecha = models.DateField()
    hora = models.TimeField()
    barbero = models.ForeignKey('Barbero', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre_completo} - {self.fecha} {self.hora}'