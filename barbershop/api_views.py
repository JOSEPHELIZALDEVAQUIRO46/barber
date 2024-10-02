from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Barberia, Barbero, Servicio, CatalogoCortes, Promociones, Contabilidad, Cita
from .serializers import BarberiaSerializer, BarberoSerializer, ServicioSerializer, CatalogoCortesSerializer, PromocionesSerializer, ContabilidadSerializer, CitaSerializer

class BarberiaViewSet(viewsets.ModelViewSet):
    queryset = Barberia.objects.all()
    serializer_class = BarberiaSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            # Serializa todos los objetos y los empaqueta en un objeto
            serializer = self.get_serializer(queryset, many=True)
            return Response({"barberias": serializer.data})  # Empaqueta los resultados en una clave "barberias"
        return Response({"detail": "No se encontró ninguna barbería."}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            barberia = Barberia.objects.get(pk=pk)
        except Barberia.DoesNotExist:
            return Response({"detail": "No se encontró ninguna barbería."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(barberia)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = BarberiaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BarberoViewSet(viewsets.ModelViewSet):
    queryset = Barbero.objects.all()
    serializer_class = BarberoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response({"barberos": serializer.data})  # Empaqueta los resultados en una clave "barberos"
        return Response({"detail": "No se encontró ningún barbero."}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            barbero = Barbero.objects.get(pk=pk)
        except Barbero.DoesNotExist:
            return Response({"detail": "No se encontró ningún barbero."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(barbero)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = BarberoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response({"servicios": serializer.data})  # Empaqueta los resultados en una clave "servicios"
        return Response({"detail": "No se encontró ningún servicio."}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            servicio = Servicio.objects.get(pk=pk)
        except Servicio.DoesNotExist:
            return Response({"detail": "No se encontró ningún servicio."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(servicio)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CatalogoCortesViewSet(viewsets.ModelViewSet):
    queryset = CatalogoCortes.objects.all()
    serializer_class = CatalogoCortesSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response({"catalogo_cortes": serializer.data})  # Empaqueta los resultados en una clave "catalogo_cortes"
        return Response({"detail": "No se encontró ningún corte."}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            catalogo_corte = CatalogoCortes.objects.get(pk=pk)
        except CatalogoCortes.DoesNotExist:
            return Response({"detail": "No se encontró ningún corte."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(catalogo_corte)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = CatalogoCortesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PromocionesViewSet(viewsets.ModelViewSet):
    queryset = Promociones.objects.all()
    serializer_class = PromocionesSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response({"promociones": serializer.data})  # Empaqueta los resultados en una clave "promociones"
        return Response({"detail": "No se encontró ninguna promoción."}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            promocion = Promociones.objects.get(pk=pk)
        except Promociones.DoesNotExist:
            return Response({"detail": "No se encontró ninguna promoción."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(promocion)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = PromocionesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContabilidadViewSet(viewsets.ModelViewSet):
    queryset = Contabilidad.objects.all()
    serializer_class = ContabilidadSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response({"contabilidad": serializer.data})  # Empaqueta los resultados en una clave "contabilidad"
        return Response({"detail": "No se encontró ninguna entrada de contabilidad."}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            contabilidad = Contabilidad.objects.get(pk=pk)
        except Contabilidad.DoesNotExist:
            return Response({"detail": "No se encontró ninguna contabilidad."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(contabilidad)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ContabilidadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response({"citas": serializer.data})  # Empaqueta los resultados en una clave "citas"
        return Response({"detail": "No se encontró ninguna cita."}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            cita = Cita.objects.get(pk=pk)
        except Cita.DoesNotExist:
            return Response({"detail": "No se encontró ninguna cita."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(cita)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = CitaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
