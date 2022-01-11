from django.db import models


# Create your models here.
class Present(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Magaz(models.Model):
    name = models.CharField(max_length=10, verbose_name='Название')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=10, verbose_name='Название')
    magaz = models.ForeignKey(Magaz, related_name='prod', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
