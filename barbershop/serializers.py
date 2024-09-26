from rest_framework import serializers
from .models import Barberia, Barbero, Servicio, CatalogoCortes, Promociones, Contabilidad, Cita

class BarberiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barberia
        fields = '__all__'

class BarberoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barbero
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class CatalogoCortesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogoCortes
        fields = '__all__'

class PromocionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promociones
        fields = '__all__'

class ContabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contabilidad
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'