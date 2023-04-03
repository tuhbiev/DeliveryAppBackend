from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория',
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):

    class Meta:
        verbose_name = 'Продукт',
        verbose_name_plural = 'Продукты'

    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=3, default='RUB')
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
