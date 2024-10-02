from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views

# Registrar las vistas
router = DefaultRouter()

# Añadir rutas para listar y crear
router.register('barberias', api_views.BarberiaViewSet, basename='barberia')
router.register('barberos', api_views.BarberoViewSet, basename='barbero')
router.register('servicios', api_views.ServicioViewSet, basename='servicio')
router.register('catalogo-cortes', api_views.CatalogoCortesViewSet, basename='catalogo-cortes')
router.register('promociones', api_views.PromocionesViewSet, basename='promocion')
router.register('contabilidad', api_views.ContabilidadViewSet, basename='contabilidad')
router.register('citas', api_views.CitaViewSet, basename='cita')

urlpatterns = [
    path('', include(router.urls)),
]
