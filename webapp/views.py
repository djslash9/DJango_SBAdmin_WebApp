from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Dashboard

# Create your views here.

def BASE(request):
    return render(request, 'base.html')

@login_required
def home(request):
    if request.user.is_superuser:
        dashboards = Dashboard.objects.all()
    else:
        dashboards = Dashboard.objects.filter(users=request.user)
    return render(request, 'home.html', {'dashboards': dashboards})

def charts(request):
    return render(request, 'charts.html')

def layoutStatic(request):
    return render(request, 'layout-static.html')

def layoutSidenavLight(request):
    return render(request, 'layout-sidenav-light.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    return render(request, 'register.html')

def password(request):
    return render(request, 'password.html')

def tables(request):
    return render(request, 'tables.html')

@login_required
def dashboard(request, dashboard_name):
    dashboard = Dashboard.objects.get(name=dashboard_name)
    if request.user not in dashboard.users.all() and not request.user.is_superuser:
        return redirect('home')
    return render(request, f'{dashboard_name.lower()}.html', {'dashboard': dashboard})