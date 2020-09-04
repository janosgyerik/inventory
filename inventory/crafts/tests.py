from django.test import TestCase

from .models import Product, Material, ProductMaterial


class ProductMaterialCostTests(TestCase):
    def test_cost_without_materials_is_zero(self):
        product = Product()
        self.assertEqual(0, product.compute_cost())

    def test_cost_with_one_material(self):
        units_per_package = 10
        price_per_package = 11

        material = Material(units_per_package=units_per_package, price_per_package=price_per_package)
        material.save()

        product = Product()
        product.save()

        pm = ProductMaterial(product=product, material=material, units=units_per_package)
        pm.save()

        self.assertEqual(price_per_package, product.compute_cost())


class MaterialCostTests(TestCase):
    def test_cost_of_0_units_is_0(self):
        self.assertEqual(0, Material(price_per_package=3, units_per_package=7).compute_cost(0))

    def test_cost_proportional_to_package_price_and_units(self):
        units_per_package = 10
        price_per_package = 16
        m = Material(price_per_package=price_per_package, units_per_package=units_per_package)

        self.assertEqual(price_per_package, m.compute_cost(units_per_package))
        self.assertEqual(price_per_package // 2, m.compute_cost(units_per_package // 2))
        self.assertEqual(price_per_package * 2, m.compute_cost(units_per_package * 2))

