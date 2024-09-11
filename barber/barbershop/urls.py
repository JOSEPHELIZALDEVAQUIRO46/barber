from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('barberias/', views.barberias, name='barberias'),
    path('barberos/', views.barberos, name='barberos'),
    path('servicios/', views.servicios, name='servicios'),
    path('contabilidad/', views.contabilidad, name='contabilidad'),
    path('promociones/', views.promociones, name='promociones'),
]