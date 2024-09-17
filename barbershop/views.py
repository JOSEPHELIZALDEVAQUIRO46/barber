from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import UserUpdateForm, ProfileUpdateForm, CustomPasswordChangeForm
from .models import Contabilidad
from .forms import ContabilidadForm


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
            return redirect('dashboard')
    return render(request, 'barbershop/login.html')

@login_required
def dashboard(request):
    return render(request, 'barbershop/dashboard.html')

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
def promociones(request):
    return render(request, 'barbershop/promociones.html')