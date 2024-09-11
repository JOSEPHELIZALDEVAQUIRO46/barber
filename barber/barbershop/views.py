from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

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
    return render(request, 'barbershop/contabilidad.html')

@login_required
def promociones(request):
    return render(request, 'barbershop/promociones.html')