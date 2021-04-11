"""HealthCompany URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "HIC Admin"
admin.site.site_title = "HIC Admin Portal"
admin.site.index_title = "Welcome to HIC Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('baseapp.urls')),
    path('hospitals/', include('hospital.urls')),
    path('patients/', include('patient.urls')),
    path('insurancecompany/', include('insurancecompany.urls')),
    path('claims/', include('claims.urls')),
    path('user/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
