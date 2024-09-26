from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Barberia, Barbero, Servicio, CatalogoCortes, Promociones, Contabilidad
from .serializers import BarberiaSerializer, BarberoSerializer, ServicioSerializer, CatalogoCortesSerializer, PromocionesSerializer, ContabilidadSerializer, CitaSerializer
from .models import Cita

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

class ContabilidadViewSet(viewsets.ModelViewSet):
    queryset = Contabilidad.objects.all()
    serializer_class = ContabilidadSerializer

    def list(self, request, *args, **kwargs):
        # Obtener el primer objeto en lugar de una lista
        contabilidad = self.get_queryset().first()

        if contabilidad is None:
            return Response({"detail": "No se encontró ninguna contabilidad."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(contabilidad)
        return Response(serializer.data)
    
class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer