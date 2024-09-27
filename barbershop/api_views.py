from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Barberia, Barbero, Servicio, CatalogoCortes, Promociones, Contabilidad, Cita
from .serializers import BarberiaSerializer, BarberoSerializer, ServicioSerializer, CatalogoCortesSerializer, PromocionesSerializer, ContabilidadSerializer, CitaSerializer

class BarberiaViewSet(viewsets.ModelViewSet):
    queryset = Barberia.objects.all()
    serializer_class = BarberiaSerializer

    def list(self, request, *args, **kwargs):
        barberia = self.get_queryset().first()
        if barberia is None:
            return Response({"detail": "No se encontró ninguna barbería."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(barberia)
        return Response(serializer.data)

class BarberoViewSet(viewsets.ModelViewSet):
    queryset = Barbero.objects.all()
    serializer_class = BarberoSerializer

    def list(self, request, *args, **kwargs):
        barbero = self.get_queryset().first()
        if barbero is None:
            return Response({"detail": "No se encontró ningún barbero."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(barbero)
        return Response(serializer.data)

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

    def list(self, request, *args, **kwargs):
        servicio = self.get_queryset().first()
        if servicio is None:
            return Response({"detail": "No se encontró ningún servicio."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(servicio)
        return Response(serializer.data)

class CatalogoCortesViewSet(viewsets.ModelViewSet):
    queryset = CatalogoCortes.objects.all()
    serializer_class = CatalogoCortesSerializer

    def list(self, request, *args, **kwargs):
        catalogo_cortes = self.get_queryset().first()
        if catalogo_cortes is None:
            return Response({"detail": "No se encontró ningún corte."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(catalogo_cortes)
        return Response(serializer.data)

class PromocionesViewSet(viewsets.ModelViewSet):
    queryset = Promociones.objects.all()
    serializer_class = PromocionesSerializer

    def list(self, request, *args, **kwargs):
        promocion = self.get_queryset().first()
        if promocion is None:
            return Response({"detail": "No se encontró ninguna promoción."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(promocion)
        return Response(serializer.data)

class ContabilidadViewSet(viewsets.ModelViewSet):
    queryset = Contabilidad.objects.all()
    serializer_class = ContabilidadSerializer

    def list(self, request, *args, **kwargs):
        contabilidad = self.get_queryset().first()
        if contabilidad is None:
            return Response({"detail": "No se encontró ninguna contabilidad."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(contabilidad)
        return Response(serializer.data)

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

    def list(self, request, *args, **kwargs):
        cita = self.get_queryset().first()
        if cita is None:
            return Response({"detail": "No se encontró ninguna cita."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(cita)
        return Response(serializer.data)
