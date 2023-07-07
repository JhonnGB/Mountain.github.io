"""proyecto_m URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from core import views as core_views
from productos import views as productos_views
from acerca import views as acerca_views
from django.conf import settings 
from registration import views as registration_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',productos_views.home,{'categoriasprod_id': 1}, name='inicio'),
    
    path('car/',core_views.car, name='car'),
    
    path('carro/', include('carro.urls')),
    
    path('pedidos/', include('pedidos.urls')),

    
    path('accounts/', include('django.contrib.auth.urls')),#IMPORTAR LA LIBRERIA PARA PODER UTILIZARLA EN EL LOGIN
    path('accounts/', include('registration.urls')),
      
    path('acerca/',acerca_views.acerca, name='acerca'),
    #url hamburguesas
    path('hamburguesa_s/',core_views.hamburguesa_s, name='hamburguesa_s'),
    path('hamburguesasuper/',core_views.hamburguesasuper, name='hamburguesasuper'),
    path('hamburguesamexi/',core_views.hamburguesamexi, name='hamburguesamexi'),
    path('hamburguesabri/',core_views.hamburguesabri, name='hamburguesabri'),
    #urls perros
    path('perrosencillo/',core_views.perrosencillo, name='perrosencillo'),
    path('perroamericano/',core_views.perroamericano, name='perroamericano'),
    path('choriperro/',core_views.choriperro, name='choriperro'),
    path('perroran/',core_views.perroran, name='perroran'),
    path('perroteque/',core_views.perroteque, name='perroteque'),
    
    #urls salchipapas
    path('salchisenci/',core_views.salchisenci, name='salchisenci'),
    path('chorisenci/',core_views.chorisenci, name='chorisenci'),
    path('salchiespe/',core_views.salchiespe, name='salchiespe'),
    path('choriespe/',core_views.choriespe, name='choriespe'),
    path('mixsuper/',core_views.mixsuper, name='mixsuper'),
    #picadas 
    path('morropla/',core_views.morropla, name='morropla'),
    path('nevatol/',core_views.nevatol, name='nevatol'),
    path('everest/',core_views.everest, name='everest'),
    path('superm/',core_views.superm, name='superm'),
    #costillas y alitas
    path('costillase/',core_views.costillase, name='costillase'),
    path('costillaes/',core_views.costillaes, name='costillaes'),
    path('costillasup/',core_views.costillasup, name='costillasup'),
    path('alitasp/',core_views.alitasp, name='alitasp'),
    path('mixta/',core_views.mixta, name='mixta'),
    
    #porciones
    path('porcionp/',core_views.porcionp, name='porcionp'),
    path('porcionh/',core_views.porcionh, name='porcionh'), 

    path('pedidos/', include('pedidos.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)