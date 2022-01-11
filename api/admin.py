from django.contrib import admin

# Register your models here.
from .models import Present, Product, Magaz

admin.site.register(Present)
admin.site.register(Product)
admin.site.register(Magaz)