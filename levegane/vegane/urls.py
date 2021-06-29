
from django.urls import path

from .views import home, receta, registrar, noticia, sesion, tip, lugar
from .views import noticiauno, noticiados, noticiatres, noticiacuatro, noticiacinco, noticiaseis, noticiasiete, noticiaocho, noticianueve

urlpatterns = [
    path('', home, name="home"),
    path('recetas/', receta, name ="receta"),
    path('registrar/', registrar, name = "registrar"),
    path('noticias/', noticia, name ="noticia"),
    path('iniciar-sesion/', sesion, name ="sesion"),
    path('tips/', tip, name ="tip"),
    path('lugares/', lugar, name ="lugar"),
    path('unilever/', noticiauno, name ="noticiauno"),
    path('vegan/', noticiados, name ="noticiauno"),
    path('mercado/', noticiatres, name ="noticiauno"),
    path('leche/', noticiacuatro, name ="noticiauno"),
    path('documental/', noticiacinco, name ="noticiauno"),
    path('china/', noticiaseis, name ="noticiauno"),
    path('beyond/', noticiasiete, name ="noticiauno"),
    path('australia/', noticiaocho, name ="noticiauno"),
    path('activismo/', noticianueve, name ="noticiauno"),
]
