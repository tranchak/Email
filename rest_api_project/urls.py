"""rest_api_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from api.views import get_presente, all_shop

router = routers.SimpleRouter()
router.register(r're_present', get_presente, basename='re_present')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('presente/', get_presente, name='presente'),
    path('shop/<int:id>', all_shop, name='all_shop'),

]
