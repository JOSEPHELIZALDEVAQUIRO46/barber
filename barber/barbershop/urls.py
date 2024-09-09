from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('barberia/<int:barberia_id>/barberos/', views.barbero_list, name='barbero_list'),
    path('servicios/', views.servicios, name='servicios'),
    path('promociones/', views.promociones, name='promociones'),
]