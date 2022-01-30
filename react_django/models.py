from django.db import models

# Create your models here.


class Car(models.Model):
    brand=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.brand

