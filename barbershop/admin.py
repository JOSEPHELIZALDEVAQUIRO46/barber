from django.contrib import admin
from .models import Barberia, Barbero, Servicio, Contabilidad, Promociones, Cita, CatalogoCortes

admin.site.register(Barberia)
admin.site.register(Barbero)
admin.site.register(Servicio)
admin.site.register(Contabilidad)
admin.site.register(Promociones)
admin.site.register(CatalogoCortes)
admin.site.register(Cita)