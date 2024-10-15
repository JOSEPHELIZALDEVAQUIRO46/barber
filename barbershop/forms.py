from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile, Contabilidad, CatalogoCortes, Cita, Barbero, Servicio, Promociones, Barberia


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'profile_picture']

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].widget.attrs = {'class': 'form-control'}

class ContabilidadForm(forms.ModelForm):
    class Meta:
        model = Contabilidad
        fields = ['fecha', 'ingresos', 'gastos']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'ingresos': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'gastos': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }

class CatalogoCorteForm(forms.ModelForm):
    class Meta:
        model = CatalogoCortes
        fields = ['barbero', 'nombre_estilo', 'imagen1', 'imagen2']
        widgets = {
            'imagen1': forms.FileInput(attrs={'accept': 'image/*'}),
            'imagen2': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['nombre_completo', 'telefono', 'fecha', 'hora', 'barbero']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['barbero'].queryset = Barbero.objects.all()
        self.fields['barbero'].label_from_instance = lambda obj: f"{obj.nombre_completo} - {obj.barberia.nombre}"

class BarberoForm(forms.ModelForm):
    class Meta:
        model = Barbero
        fields = ['usuario', 'barberia', 'certificado_profesional', 'anos_experiencia', 'especialidad', 'disponibilidad', 'nombre_completo', 'imagen_perfil']
        widgets = {
            'imagen_perfil': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'duracion_estimada', 'precio', 'imagen']
        widgets = {
            'precio': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'imagen': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class PromocionForm(forms.ModelForm):
    class Meta:
        model = Promociones
        fields = ['barberia', 'titulo', 'descripcion', 'fecha_inicio', 'fecha_fin', 'descuento', 'imagen']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
            'descuento': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'imagen': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class PromocionForm(forms.ModelForm):
    class Meta:
        model = Promociones
        fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_fin', 'descuento', 'imagen','barberia']

class BarberoForm(forms.ModelForm):
    class Meta:
        model = Barbero
        fields = ['usuario', 'barberia', 'nombre_completo', 'anos_experiencia', 'especialidad', 'disponibilidad', 'imagen_perfil', 'certificado_profesional']
        widgets = {
            'disponibilidad': forms.Textarea(attrs={'rows': 3}),
            'anos_experiencia': forms.NumberInput(attrs={'min': 0}),
        }

class BarberiaForm(forms.ModelForm):
    class Meta:
        model = Barberia
        fields = ['nombre', 'direccion', 'telefono', 'imagen_logo']

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'duracion_estimada']

class BarberiaForm(forms.ModelForm):
    class Meta:
        model = Barberia
        fields = ['nombre', 'direccion', 'telefono', 'horario_apertura', 'horario_cierre', 'descripcion', 'imagen_logo']