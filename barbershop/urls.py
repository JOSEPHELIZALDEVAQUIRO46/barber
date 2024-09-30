from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('barberias/', views.barberias, name='barberias'),
    path('barberos/', views.barberos, name='barberos'),
    path('servicios/', views.servicios, name='servicios'),
    path('contabilidad/', views.contabilidad, name='contabilidad'),
    path('contabilidad/actualizar/<int:pk>/', views.actualizar_contabilidad, name='actualizar_contabilidad'),
    path('contabilidad/eliminar/<int:pk>/', views.eliminar_contabilidad, name='eliminar_contabilidad'),
    path('promociones/', views.promociones, name='promociones'),
    path('profile/', views.profile, name='profile'),
    path('profile/change-password/', views.change_password, name='change_password'),
    path('catalogo-cortes/', views.catalogo_cortes, name='catalogo_cortes'),
    path('catalogo-cortes/eliminar/<int:pk>/', views.eliminar_corte, name='eliminar_corte'),
    path('citas/', views.citas, name='citas'),
    path('citas/eliminar/<int:pk>/', views.eliminar_cita, name='eliminar_cita'),
]