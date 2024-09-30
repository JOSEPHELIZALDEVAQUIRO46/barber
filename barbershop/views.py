from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import UserUpdateForm, ProfileUpdateForm, CustomPasswordChangeForm
from .models import Contabilidad, CatalogoCortes, Cita, Barbero
from .forms import ContabilidadForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'barbershop/profile.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Tu contraseña ha sido actualizada!')
            return redirect('profile')
        else:
            messages.error(request, 'Por favor corrige los errores abajo.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'barbershop/change_password.html', {'form': form})


def home(request):
    return render(request, 'barbershop/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('barberias')
    return render(request, 'barbershop/login.html')


@login_required
def barberias(request):
    return render(request, 'barbershop/barberias.html')

@login_required
def barberos(request):
    return render(request, 'barbershop/barberos.html')

@login_required
def servicios(request):
    return render(request, 'barbershop/servicios.html')

@login_required
def contabilidad(request):
    if request.method == 'POST':
        form = ContabilidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos de contabilidad agregados exitosamente.')
            return redirect('contabilidad')
    else:
        form = ContabilidadForm()

    # Obtener los últimos 12 meses de datos
    datos = Contabilidad.objects.order_by('-fecha')[:12]
   
    # Preparar datos para la gráfica
    labels = [dato.fecha.strftime('%B %Y') for dato in reversed(datos)]
    ingresos = [float(dato.ingresos) for dato in reversed(datos)]
    gastos = [float(dato.gastos) for dato in reversed(datos)]
    beneficios = [float(dato.beneficio) for dato in reversed(datos)]
    
    context = {
        'form': form,
        'datos': datos,
        'labels': labels,
        'ingresos': ingresos,
        'gastos': gastos,
        'beneficios': beneficios,
    }
    return render(request, 'barbershop/contabilidad.html', context)

@login_required
def actualizar_contabilidad(request, pk):
    dato = get_object_or_404(Contabilidad, pk=pk)
    if request.method == 'POST':
        form = ContabilidadForm(request.POST, instance=dato)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos de contabilidad actualizados exitosamente.')
            return redirect('contabilidad')
    else:
        form = ContabilidadForm(instance=dato)
    
    context = {
        'form': form,
        'dato': dato,
    }
    return render(request, 'barbershop/actualizar_contabilidad.html', context)

@login_required
def eliminar_contabilidad(request, pk):
    dato = get_object_or_404(Contabilidad, pk=pk)
    if request.method == 'POST':
        dato.delete()
        messages.success(request, 'Datos de contabilidad eliminados exitosamente.')
        return redirect('contabilidad')
    
    context = {
        'dato': dato,
    }
    return render(request, 'barbershop/eliminar_contabilidad.html', context)
@login_required
def promociones(request):
    return render(request, 'barbershop/promociones.html')

@login_required
def catalogo_cortes(request):
    cortes = CatalogoCortes.objects.all()
    if request.method == 'POST':
        form = CatalogoCorteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nuevo corte agregado al catálogo.')
            return redirect('catalogo_cortes')
    else:
        form = CatalogoCorteForm()
    
    context = {
        'cortes': cortes,
        'form': form,
    }
    return render(request, 'barbershop/catalogo_cortes.html', context)

@login_required
def eliminar_corte(request, pk):
    corte = get_object_or_404(CatalogoCortes, pk=pk)
    if request.method == 'POST':
        corte.delete()
        messages.success(request, 'Corte eliminado del catálogo.')
        return redirect('catalogo_cortes')
    return render(request, 'barbershop/eliminar_corte.html', {'corte': corte})

@login_required
def citas(request):
    citas_futuras = Cita.objects.filter(fecha__gte=timezone.now().date()).order_by('fecha', 'hora')
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nueva cita agendada.')
            return redirect('citas')
    else:
        form = CitaForm()
    
    context = {
        'citas': citas_futuras,
        'form': form,
    }
    return render(request, 'barbershop/citas.html', context)

@login_required
def eliminar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        messages.success(request, 'Cita eliminada.')
        return redirect('citas')
    return render(request, 'barbershop/eliminar_cita.html', {'cita': cita})