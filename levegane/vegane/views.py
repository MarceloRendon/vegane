from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'vegane/index.html')

def registrar(request):
    return render(request, 'vegane/registrar.html')

def receta(request):
    return render(request, 'vegane/recetas.html')

def noticia(request):
    return render(request, 'vegane/noticias.html')

def sesion(request):
    return render(request, 'vegane/iniciar-sesion.html')

def tip(request):
    return render(request, 'vegane/tips.html')

def lugar(request):
    return render(request, 'vegane/lugares.html')

# def vistas pag de noticias
def noticiauno(request):
    return render(request, 'vegane/noticias/unilever.html')

def noticiados(request):
    return render(request, 'vegane/noticias/vegan.html')

def noticiatres(request):
    return render(request, 'vegane/noticias/mercadovegano.html')

def noticiacuatro(request):
    return render(request, 'vegane/noticias/leche.html')

def noticiacinco(request):
    return render(request, 'vegane/noticias/documental.html')

def noticiaseis(request):
    return render(request, 'vegane/noticias/china.html')
    
def noticiasiete(request):
    return render(request, 'vegane/noticias/beyond.html')


def noticiaocho(request):
    return render(request, 'vegane/noticias/australia.html')


def noticianueve(request):
    return render(request, 'vegane/noticias/activismo.html')


#def vista de recetas
def recetauno(request):
    return render(request, 'vegane/recetasitios/sandwich-no-pollo.html')

def recetados(request):
    return render(request, 'vegane/recetasitios/ricotta-de-mani.html')

def recetatres(request):
    return render(request, 'vegane/recetasitios/harina-de-garbanzos.html')

def recetacuatro(request):
    return render(request, 'vegane/recetasitios/ensalada-de-garbanzos.html')

def recetacinco(request):
    return render(request, 'vegane/recetasitios/budin-de-algarroba.html')

def recetaseis(request):
    return render(request, 'vegane/recetasitios/ceviche-de-champiniones.html')

def recetasiete(request):
    return render(request, 'vegane/recetasitios/champiniones-rellenos.html')

def recetaocho(request):
    return render(request, 'vegane/recetasitios/carpaccio-de-verduras.html')

def recetanueve(request):
    return render(request, 'vegane/recetasitios/pizzetas-de-zapallo-italiano.html')

def recetadiez(request):
    return render(request, 'vegane/recetasitios/croqueta-de-zanahoria.html')

def recetaonce(request):
    return render(request, 'vegane/recetasitios/ensalada-griega.html')

def recetadoce(request):
    return render(request, 'vegane/recetasitios/ensalada-de-quinoa.html')

