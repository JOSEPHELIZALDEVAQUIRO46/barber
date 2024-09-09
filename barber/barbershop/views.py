from django.shortcuts import render, get_object_or_404
from .models import Barberia, Barbero, Servicio, Promociones

def home(request):
    barberias = Barberia.objects.all()
    return render(request, 'barbershop/home.html', {'barberias': barberias})

def barbero_list(request, barberia_id):
    barberia = get_object_or_404(Barberia, id=barberia_id)
    barberos = Barbero.objects.filter(barberia=barberia)
    return render(request, 'barbershop/barbero_list.html', {'barberia': barberia, 'barberos': barberos})

def servicios(request):
    servicios_list = Servicio.objects.all()
    return render(request, 'barbershop/servicios.html', {'servicios': servicios_list})

def promociones(request):
    promociones_list = Promociones.objects.all()
    return render(request, 'barbershop/promociones.html', {'promociones': promociones_list})

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