from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [

    path('accaunt', ApiUserRegistartionView.as_view(), name='accaunt')


]
