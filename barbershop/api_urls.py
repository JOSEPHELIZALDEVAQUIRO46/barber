from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register(r'barberias', api_views.BarberiaViewSet)
router.register(r'barberos', api_views.BarberoViewSet)
router.register(r'servicios', api_views.ServicioViewSet)
router.register(r'catalogo-cortes', api_views.CatalogoCortesViewSet)
router.register(r'promociones', api_views.PromocionesViewSet)
router.register(r'contabilidad', api_views.ContabilidadViewSet)
router.register(r'citas', api_views.CitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]