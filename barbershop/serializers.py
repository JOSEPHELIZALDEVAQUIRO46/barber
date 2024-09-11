from rest_framework import serializers
from .models import Barberia, Barbero, Servicio, CatalogoCortes, Promociones

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