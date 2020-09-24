from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext as _


class Material(models.Model):
    name = models.CharField(max_length=250)
    sku = models.CharField(max_length=50, unique=True)
    size = models.CharField(max_length=100, blank=True)
    price_per_package = models.FloatField()
    units_per_package = models.FloatField()
    vendor_url = models.URLField(help_text=_("Vendor / website URL to buy more"), blank=True, null=True)
    stock = models.FloatField(help_text=_("Available units / amount"), default=0)
    memo = models.TextField(blank=True)
    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)

    def compute_cost(self, units):
        return units * self.price_per_package / self.units_per_package

    def __str__(self):
        return f"{self.name} ({self.units_per_package} units/package)"


class MaterialTag(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.tag


class Product(models.Model):
    name = models.CharField(max_length=250)
    sku = models.CharField(max_length=50, unique=True)
    size = models.CharField(max_length=100, blank=True)
    hours_to_make = models.FloatField(blank=True, null=True)
    target_price = models.FloatField(blank=True, null=True)
    stock = models.IntegerField(help_text=_("Available items to sell"), default=0)
    memo = models.TextField(blank=True)
    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.name

    def compute_cost(self):
        return sum(pm.compute_cost() for pm in self.productmaterial_set.all())


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    units = models.FloatField()
    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)

    def compute_cost(self):
        return self.material.compute_cost(self.units)

    def __str__(self):
        return f"{self.product} - {self.material} - {self.units}"


class ProductTag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.tag
