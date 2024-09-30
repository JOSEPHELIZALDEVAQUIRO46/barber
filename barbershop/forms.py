from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile
from .models import Profile, Contabilidad, CatalogoCortes, Cita, Barbero


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
        }

class CatalogoCorteForm(forms.ModelForm):
    class Meta:
        model = CatalogoCortes
        fields = ['barbero', 'nombre_estilo', 'imagen']
        widgets = {
            'imagen': forms.FileInput(attrs={'accept': 'image/*'}),
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
        self.fields['barbero'].label_from_instance = lambda obj: f"{obj.usuario.get_full_name()} - {obj.barberia.nombre}"