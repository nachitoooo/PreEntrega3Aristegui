from django import forms
from .models import Director, Preceptor

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo Electrónico',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Escribe el nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Escribe el apellido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Escribe el correo electrónico'}),

        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        return apellido

class PreceptorForm(forms.ModelForm):
    class Meta:
        model = Preceptor
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo Electrónico',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Escribe el nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Escribe el apellido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Escribe el correo electrónico'}),

        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']

        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        return apellido
from django import forms
from .models import Profesor

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo Electrónico',
            'profesion': 'Profesión',
        
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Escribe el nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Escribe el apellido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Escribe el correo electrónico'}),
            'profesion': forms.TextInput(attrs={'placeholder': 'Escribe la profesión'}),

        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        return apellido

    def clean_email(self):
        email = self.cleaned_data['email']
        return email
