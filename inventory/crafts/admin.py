from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Material, Product, ProductMaterial, ProductTag, MaterialTag


class MaterialInline(admin.TabularInline):
    model = ProductMaterial
    exclude = ['created_at', 'updated_at']
    extra = 1


class ProductTagInline(admin.TabularInline):
    model = ProductTag
    exclude = ['created_at', 'updated_at']
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductTagInline, MaterialInline]
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
    extra = 3


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    inlines = [MaterialTagInline, ProductInline]
    exclude = ['created_at', 'updated_at']
    list_display = ['name', 'sku', 'tags', 'price_per_package', 'units_per_package', 'stock', 'vendor_link']

    def tags(self, obj):
        return ', '.join([pt.tag for pt in obj.materialtag_set.all()])

    def vendor_link(self, obj):
        if obj.vendor_url:
            return mark_safe(f'<a href="{obj.vendor_url}">{obj.vendor_url}</a>')
        else:
            return None
