# barbershop/models.py

from django.db import models
from django.contrib.auth.models import User

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
    imagen = models.ImageField(upload_to='servicios/', null=True, blank=True)  # Nueva línea

    def __str__(self):
        return self.nombre

class CatalogoCortes(models.Model):
    barbero = models.ForeignKey(Barbero, on_delete=models.CASCADE)
    nombre_estilo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='catalogo_cortes/')

    def __str__(self):
        return f"{self.nombre_estilo} - {self.barbero.usuario.get_full_name()}"

class Resena(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    barbero = models.ForeignKey(Barbero, on_delete=models.CASCADE)
    calificacion = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField()
    fecha_resena = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.cliente.get_full_name()} para {self.barbero.usuario.get_full_name()}"

class Pago(models.Model):
    METODOS_PAGO = [
        ('efectivo', 'Efectivo'),
        ('nequi', 'Nequi'),
    ]
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    barbero = models.ForeignKey(Barbero, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    estado_pago = models.BooleanField(default=False)

    def __str__(self):
        return f"Pago de {self.cliente.get_full_name()} a {self.barbero.usuario.get_full_name()}"

class BarberFace(models.Model):
    barbero = models.ForeignKey(Barbero, on_delete=models.CASCADE, null=True, blank=True)  # Permite nulos temporalmente
    imagen_rostro = models.ImageField(upload_to='barberface/')
    fecha_escaneo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.barbero:
            return f"BarberFace de {self.barbero.usuario.get_full_name()}"
        return "BarberFace sin barbero asignado"

class EstilosSugeridos(models.Model):
    barberface = models.ForeignKey(BarberFace, on_delete=models.CASCADE)
    corte = models.ForeignKey(CatalogoCortes, on_delete=models.CASCADE)
    porcentaje_coincidencia = models.FloatField()

    def __str__(self):
        return f"Sugerencia para {self.barberface.barbero.usuario.get_full_name()}"

class RankingBarberos(models.Model):
    barbero = models.OneToOneField(Barbero, on_delete=models.CASCADE)
    puntuacion_promedio = models.FloatField()
    total_resenas = models.IntegerField()
    posicion_ranking = models.IntegerField()

    def __str__(self):
        return f"Ranking de {self.barbero.usuario.get_full_name()}"

class Contabilidad(models.Model):
    barberia = models.ForeignKey(Barberia, on_delete=models.CASCADE)
    fecha = models.DateField()
    ingresos_totales = models.DecimalField(max_digits=10, decimal_places=2)
    gastos_totales = models.DecimalField(max_digits=10, decimal_places=2)
    ganancia_neta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Contabilidad de {self.barberia.nombre} - {self.fecha}"

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