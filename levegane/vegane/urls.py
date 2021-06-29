
from django.urls import path

from .views import home, receta, registrar, noticia, sesion, tip, lugar, noticiauno

urlpatterns = [
    path('', home, name="home"),
    path('recetas/', receta, name ="receta"),
    path('registrar/', registrar, name = "registrar"),
    path('noticias/', noticia, name ="noticia"),
    path('iniciar-sesion/', sesion, name ="sesion"),
    path('tips/', tip, name ="tip"),
    path('lugares/', lugar, name ="lugar"),
    path('unilever/', noticiauno, name ="noticiauno"),
]
