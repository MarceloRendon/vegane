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


