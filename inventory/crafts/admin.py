from django.contrib import admin

from .models import Material, Product, ProductMaterial, ProductTag, MaterialTag


class MaterialInline(admin.TabularInline):
    model = ProductMaterial
    exclude = ['created_at', 'updated_at']
    extra = 1


class ProductTagInline(admin.TabularInline):
    model = ProductTag
    exclude = ['created_at', 'updated_at']
    extra = 2


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [MaterialInline, ProductTagInline]
    exclude = ['created_at', 'updated_at']
    list_display = ['name', 'sku', 'tags', 'stock', 'compute_cost']
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


class MaterialTagInline(admin.TabularInline):
    model = MaterialTag
    exclude = ['created_at', 'updated_at']
    extra = 2


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    inlines = [ProductInline, MaterialTagInline]
    exclude = ['created_at', 'updated_at']
    list_display = ['name', 'sku', 'tags', 'price_per_package', 'units_per_package', 'stock']

    def tags(self, obj):
        return ', '.join([pt.tag for pt in obj.materialtag_set.all()])
