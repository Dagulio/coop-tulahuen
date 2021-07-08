from django import forms
from .models import Producto, Usuario, Registro
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import Select
from asgiref.sync import sync_to_async


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields = [
            'nombre',
            'disponibilidad',
        ]

        labels = {
            'nombre': 'Nombre',
            'disponibilidad': 'Disponibilidad',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'disponibilidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class AporteForm(forms.ModelForm):
    class Meta:
        model = Registro

        fields = [
            'producto',
            'cantidad',
            'socioAportador',
            'cliente',
        ]

        labels = {
            'producto': 'Producto',
            'cantidad': 'Cantidad',
            'socioAportador': 'Socio',
            'cliente': 'Cliente',
        }

        widgets = {
            'producto': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'socioAportador': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UsuarioPForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioPForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget = forms.PasswordInput(attrs={'class': 'form-control',
                                                                       'autocomplete': 'new-password'})

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'rut',
            'email',
            'razonSocial',
            'password1',
            'password2',
            'esSocio',
        ]

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'rut': 'Rut',
            'email': 'Email',
            'razonSocial': 'Razon Social',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
            'esSocio': '¿Es Socio?',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'razonSocial': forms.TextInput(attrs={'class': 'form-control'}),
            'esSocio': forms.CheckboxInput(),
        }
