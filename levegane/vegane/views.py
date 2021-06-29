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
