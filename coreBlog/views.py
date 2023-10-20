from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm ,LoginForm , PostForm , CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import ListView , DetailView
from django.utils.decorators import method_decorator


@login_required(login_url='main:login')
def baseview(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.errors)
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('main:inicio')
    else:
        
        form = CustomUserCreationForm()
    #context = {'form' : form}
    return render(request,'register.html')

@method_decorator(login_required(login_url='main:login'),name='dispatch')
class Inicio(ListView):
    model = Post
    template_name = "inicio.html"
    context_object_name = 'posts'
    # Agrega esta función para manejar solicitudes POST
    def post(self, request, *args, **kwargs):
        post_form = PostForm(request.POST,request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            # También podrías redirigir a la página de inicio o a donde prefieras
            return redirect('main:inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_form'] = PostForm()  # Agrega el formulario al contexto
        return context
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-created_at')[:10]

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                # Realiza la redirección deseada después del inicio de sesión
                return redirect('main:inicio')
        else:
            # Las credenciales no son válidas, mostrar un mensaje de error
            messages.warning(request, 'Credenciales inválidas')
            return redirect('main:login')
    return render(request, 'login.html')

def salir(request):
    logout(request)
    # Redirigir a la página de inicio o al lugar que quieras después del cierre de sesión
    return redirect('main:login')

@login_required(login_url='main:login')
def private_profile(request):
    user= request.user
    
    follower = user.follower.count()
    followed = user.followed.count()

    return render(request, 'private_profile.html',{'user':user,'followers':follower,'followed':followed})

@method_decorator(login_required(login_url='main:login'),name='dispatch')
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'  # Define el nombre de la variable de contexto

    def comment(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST,request.FILES)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.save()
            return redirect('main:post_detail')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Recupera los comentarios relacionados con el post actual
        post = self.get_object()
        comments = Comment.objects.filter(post=post)

        # Agrega los comentarios al contexto
        context['comments'] = comments

        return context

