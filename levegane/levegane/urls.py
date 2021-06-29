"""levegane URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vegane.urls')),
    path('recetas/', include('vegane.urls')),
    path('registrar/', include('vegane.urls')),
    path('noticias/', include('vegane.urls')),
    path('lugares/', include('vegane.urls')),
    path('tips/', include('vegane.urls')),
    path('unilever/', include('vegane.urls')),
    path('vegan/', include('vegane.urls')),
    path('mercado/', include('vegane.urls')),
    path('leche/', include('vegane.urls')),
    path('documental/', include('vegane.urls')),
    path('china/', include('vegane.urls')),
    path('beyond/', include('vegane.urls')),
    path('australia/', include('vegane.urls')),
    path('activismo/', include('vegane.urls')),

]
