from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BarberiaViewSet, BarberoViewSet, ServicioViewSet, CatalogoCortesViewSet, PromocionesViewSet

router = DefaultRouter()
router.register(r'barberias', BarberiaViewSet)
router.register(r'barberos', BarberoViewSet)
router.register(r'servicios', ServicioViewSet)
router.register(r'catalogo-cortes', CatalogoCortesViewSet)
router.register(r'promociones', PromocionesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]