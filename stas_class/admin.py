from django.contrib import admin

# Register your models here.
from .models import Zawod, Product

admin.site.register(Zawod)
admin.site.register(Product)
