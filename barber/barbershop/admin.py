from django.contrib import admin
from .models import Barberia, Barbero, Servicio, Contabilidad, DetalleContabilidad, Ubicacion, Promociones

class DetalleContabilidadInline(admin.TabularInline):
    model = DetalleContabilidad
    extra = 1

@admin.register(Contabilidad)
class ContabilidadAdmin(admin.ModelAdmin):
    inlines = [DetalleContabilidadInline]

admin.site.register(Barberia)
admin.site.register(Barbero)
admin.site.register(Servicio)
admin.site.register(Ubicacion)
admin.site.register(Promociones)