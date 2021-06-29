
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
    path('vegan/', noticiados, name ="noticiados"),
    path('mercado/', noticiatres, name ="noticiatres"),
    path('leche/', noticiacuatro, name ="noticiacuatro"),
    path('documental/', noticiacinco, name ="noticiacinco"),
    path('china/', noticiaseis, name ="noticiaseis"),
    path('beyond/', noticiasiete, name ="noticiasiete"),
    path('australia/', noticiaocho, name ="noticiaocho"),
    path('activismo/', noticianueve, name ="noticianueve"),
]
