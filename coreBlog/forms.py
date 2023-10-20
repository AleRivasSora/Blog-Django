from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile , Post , Comment
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    # Agrega campos personalizados aquí si es necesario
    foto = forms.ImageField(required=False, help_text='Sube tu foto de perfil')
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña',widget=forms.PasswordInput)
    class Meta:
        model = UserProfile
        fields = ('username','first_name','last_name','email','edad','descripcion','sexo')
        help_texts = {k:"" for k in fields}


class LoginForm(AuthenticationForm):
    # Agrega campos adicionales si es necesario

    class Meta:
        model = UserProfile  # Establece el modelo personalizado

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content','image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text','image_post']