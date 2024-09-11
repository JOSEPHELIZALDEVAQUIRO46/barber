# barbershop/api_views.py

from rest_framework import viewsets
from .models import Barberia, Barbero, Servicio, CatalogoCortes, Promociones
from .serializers import BarberiaSerializer, BarberoSerializer, ServicioSerializer, CatalogoCortesSerializer, PromocionesSerializer

class BarberiaViewSet(viewsets.ModelViewSet):
    queryset = Barberia.objects.all()
    serializer_class = BarberiaSerializer

class BarberoViewSet(viewsets.ModelViewSet):
    queryset = Barbero.objects.all()
    serializer_class = BarberoSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class CatalogoCortesViewSet(viewsets.ModelViewSet):
    queryset = CatalogoCortes.objects.all()
    serializer_class = CatalogoCortesSerializer

class PromocionesViewSet(viewsets.ModelViewSet):
    queryset = Promociones.objects.all()
    serializer_class = PromocionesSerializer