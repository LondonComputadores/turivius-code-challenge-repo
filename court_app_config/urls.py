"""court_app_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from court_app.views import LawsuitViewSet
from rest_framework import routers
from court_app import views

router = routers.DefaultRouter()
router.register(r'lawsuits', LawsuitViewSet)
router.register(r'lawsuits/status', LawsuitViewSet)

urlpatterns = [
    path('', include(router.urls)), # router may be replaced by court_app if wished
    path('admin/', admin.site.urls),
    path('status/', views.status, name='status'),
]
