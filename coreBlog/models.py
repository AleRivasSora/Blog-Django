from django.db import models
from datetime import datetime

class Type(models.Model):
    names = models.CharField(max_length=100,verbose_name='nombre')

    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name = 'tipo'
        verbose_name_plural = 'tipos'
        ordering = ['id']

class Empleado(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=150,verbose_name='Nombres')
    cedula = models.CharField(max_length=8,unique=True,verbose_name='Cedula')
    date_joined = models.DateField(default=datetime.now,verbose_name='Fecha de registro')
    date_created = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    edad = models.PositiveIntegerField(default=0,max_length=2)
    salario = models.DecimalField(default=0.000,max_digits=15,decimal_places=2)
    state = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%D',null=True,blank=True)
    cv = models.ImageField(upload_to='CVs/%Y/%m/%D',null=True,blank=True)

    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name = ' empleado'
        verbose_name_plural = 'empleados'
        ordering = ['id']