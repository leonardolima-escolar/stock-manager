from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Product(models.Model):
    name = models.CharField('nome', max_length=32, unique=True)
    price = models.FloatField('preço', validators=[MinValueValidator(0.0)])
    quantity = models.PositiveIntegerField('quantidade')


    def __str__(self):
        return self.name
