"""
URL configuration for sclassdev project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app_landing.views import landing_page  # Import view dari app_landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='home'),  # Halaman utama langsung ke index.html di app_landing
    path('landing/', include('app_landing.urls')),  # Jika ingin tetap akses /landing/
]
