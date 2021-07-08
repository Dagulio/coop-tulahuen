from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='Home'),
    path('login/', LoginView.as_view(template_name='inventario_cooperativa/user/login.html', redirect_authenticated_user=True, ), name='Login'),
    path('logout/', auth_views.logout_then_login, name='Logout'),
    path('agregarProducto/', views.agregar_producto, name='Agregar'),
    path('generarAporte/', views.generar_aporte, name='Aporte'),
    path('registrarUsuario/', views.registrar_usuario, name='Registrar'),
    path('listaProductos/', views.listar_inventario, name='Lista_Inventario'),
    path('listaRegistros/', views.listar_registros, name='Lista_Registros'),
    path('listaSocios/', views.listar_socios, name='Lista_Socios'),
    path('privacy/', views.privacidad, name='Privacidad'),
    path('legal/', views.legal, name='Legal'),
    path('cookies/', views.cookies, name='Cookies'),
    path('contacto/', views.contacto, name='Contacto'),
]
