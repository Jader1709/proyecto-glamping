from django.db import models
from decimal import Decimal

class Service(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name