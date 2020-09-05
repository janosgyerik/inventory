from django.contrib import admin

from .models import Material, Product, ProductMaterial, ProductTag


class MaterialInline(admin.TabularInline):
    model = ProductMaterial
    exclude = ['created_at', 'updated_at']
    extra = 3


class ProductTagInline(admin.TabularInline):
    model = ProductTag
    exclude = ['created_at', 'updated_at']
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [MaterialInline, ProductTagInline]
    exclude = ['created_at', 'updated_at']
    list_display = ['name', 'tags', 'sku', 'stock', 'compute_cost']
    list_filter = ['producttag']

    def tags(self, obj):
        return ', '.join([pt.tag for pt in obj.producttag_set.all()])


class ProductInline(admin.TabularInline):
    model = ProductMaterial
    exclude = ['created_at', 'updated_at']
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    exclude = ['created_at', 'updated_at']
    list_display = ['name', 'sku', 'price_per_package', 'units_per_package', 'stock']
