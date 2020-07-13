from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField(default=1000, validators=[MinValueValidator(1)])
    discount = models.DecimalField(default=0.0, max_digits=4, decimal_places=3)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
