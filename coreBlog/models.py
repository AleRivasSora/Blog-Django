from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from blogProyecto.settings import MEDIA_URL, STATIC_URL
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

class UserProfile(AbstractUser):
    foto = models.ImageField(upload_to='fotos/%Y/%m/%D',null=True,blank=True,verbose_name='Foto')
    edad = models.PositiveIntegerField(verbose_name='edad')
    descripcion = models.TextField(max_length=400,verbose_name='Descripcion')
    lista_sexo = [('M','Hombre'),('F','Mujer')]
    sexo = models.CharField(max_length=20,choices=lista_sexo)

    def get_foto(self):
        if self.foto:
            return '{}{}'.format(MEDIA_URL,self.foto)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        ordering = ['id']
        

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='fotos_post/%Y/%m/%D',null=True,blank=True,verbose_name='Foto')
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_post = models.ImageField(upload_to='fotos_post/%Y/%m/%D',null=True,blank=True,verbose_name='Foto')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

class Follower(models.Model):
    follower = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"