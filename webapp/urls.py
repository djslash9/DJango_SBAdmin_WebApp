from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('charts/', views.charts, name='charts'),
    path('layoutStatic/', views.layoutStatic, name='layoutStatic'),
    path('layoutSidenavLight/', views.layoutSidenavLight, name='layoutSidenavLight'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('password/', views.password, name='password'),
    path('tables/', views.tables, name='tables'),
    path('<str:dashboard_name>/', views.dashboard, name='dashboard'),
]