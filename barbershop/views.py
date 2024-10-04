from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.decorators.cache import never_cache
from .forms import (UserUpdateForm, ProfileUpdateForm, CustomPasswordChangeForm, 
                    ContabilidadForm, CatalogoCorteForm, CitaForm, BarberoForm, 
                    ServicioForm, PromocionForm, BarberiaForm)
from .models import (Contabilidad, CatalogoCortes, Cita, Barbero, Servicio, 
                     Promociones, Barberia)


def home(request):
    if request.user.is_authenticated:
        return redirect('barberias')
    return render(request, 'barbershop/home.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('barberias')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['is_valid'] = True
            return redirect('barberias')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'barbershop/login.html')

@require_POST
@never_cache
@login_required
def logout_view(request):
    logout(request)
    response = redirect('home')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

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




@login_required
def barberias(request):
    barberias = Barberia.objects.all()
    return render(request, 'barbershop/barberias.html', {'barberias': barberias})

@login_required
def agregar_barberia(request):
    if request.method == 'POST':
        form = BarberiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Barbería agregada exitosamente.')
            return redirect('barberias')
    else:
        form = BarberiaForm()
    return render(request, 'barbershop/agregar_barberia.html', {'form': form})

@login_required
def editar_barberia(request, pk):
    barberia = get_object_or_404(Barberia, pk=pk)
    if request.method == 'POST':
        form = BarberiaForm(request.POST, request.FILES, instance=barberia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Barbería actualizada exitosamente.')
            return redirect('barberias')
    else:
        form = BarberiaForm(instance=barberia)
    return render(request, 'barbershop/editar_barberia.html', {'form': form})

@login_required
def eliminar_barberia(request, pk):
    barberia = get_object_or_404(Barberia, pk=pk)
    if request.method == 'POST':
        barberia.delete()
        messages.success(request, 'Barbería eliminada exitosamente.')
        return redirect('barberias')
    return render(request, 'barbershop/eliminar_barberia.html', {'barberia': barberia})

@login_required
def barberos(request):
    barberos = Barbero.objects.all()
    return render(request, 'barbershop/barberos.html', {'barberos': barberos})

@login_required
def agregar_barbero(request):
    if request.method == 'POST':
        form = BarberoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Barbero agregado exitosamente.')
            return redirect('barberos')
    else:
        form = BarberoForm()
    return render(request, 'barbershop/agregar_barbero.html', {'form': form})

@login_required
def editar_barbero(request, pk):
    barbero = get_object_or_404(Barbero, pk=pk)
    if request.method == 'POST':
        form = BarberoForm(request.POST, request.FILES, instance=barbero)
        if form.is_valid():
            form.save()
            messages.success(request, 'Barbero actualizado exitosamente.')
            return redirect('barberos')
    else:
        form = BarberoForm(instance=barbero)
    return render(request, 'barbershop/editar_barbero.html', {'form': form})

@login_required
def eliminar_barbero(request, pk):
    barbero = get_object_or_404(Barbero, pk=pk)
    if request.method == 'POST':
        barbero.delete()
        messages.success(request, 'Barbero eliminado exitosamente.')
        return redirect('barberos')
    return render(request, 'barbershop/eliminar_barbero.html', {'barbero': barbero})
@login_required
def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'barbershop/servicios.html', {'servicios': servicios})

@login_required
def agregar_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Servicio agregado exitosamente.')
            return redirect('servicios')
    else:
        form = ServicioForm()
    return render(request, 'barbershop/agregar_servicio.html', {'form': form})

@login_required
def editar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES, instance=servicio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Servicio actualizado exitosamente.')
            return redirect('servicios')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'barbershop/editar_servicio.html', {'form': form})

@login_required
def eliminar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        servicio.delete()
        messages.success(request, 'Servicio eliminado exitosamente.')
        return redirect('servicios')
    return render(request, 'barbershop/eliminar_servicio.html', {'servicio': servicio})

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

    datos = Contabilidad.objects.order_by('-fecha')[:12]
   
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
    promociones = Promociones.objects.all()
    if request.method == 'POST':
        form = PromocionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nueva promoción agregada exitosamente.')
            return redirect('promociones')
    else:
        form = PromocionForm()
    context = {'promociones': promociones, 'form': form}
    return render(request, 'barbershop/promociones.html', context)

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


@login_required
def promociones(request):
    promociones = Promociones.objects.all()
    return render(request, 'barbershop/promociones.html', {'promociones': promociones})

@login_required
def agregar_promocion(request):
    if request.method == 'POST':
        form = PromocionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Promoción agregada exitosamente.')
            return redirect('promociones')
    else:
        form = PromocionForm()
    return render(request, 'barbershop/agregar_promocion.html', {'form': form})

@login_required
def editar_promocion(request, pk):
    promocion = get_object_or_404(Promociones, pk=pk)
    if request.method == 'POST':
        form = PromocionForm(request.POST, request.FILES, instance=promocion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Promoción actualizada exitosamente.')
            return redirect('promociones')
    else:
        form = PromocionForm(instance=promocion)
    return render(request, 'barbershop/editar_promocion.html', {'form': form})

@login_required
def eliminar_promocion(request, pk):
    promocion = get_object_or_404(Promociones, pk=pk)
    if request.method == 'POST':
        promocion.delete()
        messages.success(request, 'Promoción eliminada exitosamente.')
        return redirect('promociones')
    return render(request, 'barbershop/eliminar_promocion.html', {'promocion': promocion})
