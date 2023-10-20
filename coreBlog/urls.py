from django.urls import path
from coreBlog import views 
from coreBlog.views import Inicio, PostDetailView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'
urlpatterns = [
    path('', views.baseview, name='index'),
    path('register',views.register, name='register'),
    path('login',views.login,name='login'),
    path('inicio',Inicio.as_view(),name='inicio'),
    path('salir',views.salir,name='salir'),
    path('private_profile',views.private_profile,name='private_profile'),
    path('post/<int:pk>/<str:author>', PostDetailView.as_view(),name='post_detail'),
    path('profile/<str:author>', views.public_profile, name='public_profile'),
    
    # otras URLs de la aplicación
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)