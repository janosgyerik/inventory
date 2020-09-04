from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext as _


class Material(models.Model):
    name = models.CharField(max_length=50)
    price_per_package = models.FloatField()
    units_per_package = models.FloatField()
    vendor_url = models.URLField(help_text=_("Vendor / website URL to buy more"), blank=True)
    stock = models.FloatField(help_text=_("Available units / amount"), default=0)
    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    hours_to_make = models.FloatField(blank=True)
    target_price = models.FloatField(blank=True)
    stock = models.IntegerField(help_text=_("Available items to sell"), default=0)
    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.name


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    units = models.FloatField()
    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return f"{self.product} - {self.material} - {self.units}"
