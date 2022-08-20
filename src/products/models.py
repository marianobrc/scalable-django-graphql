from django.db import models
from model_utils.models import UUIDModel, TimeStampedModel


class Category(UUIDModel, TimeStampedModel):
    name = models.CharField(db_index=True, max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(UUIDModel, TimeStampedModel):
    title = models.CharField(db_index=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(max_length=3, default="USD")
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE, related_name='products')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
