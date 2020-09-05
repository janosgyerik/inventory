from django.contrib import admin
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe

from .models import Material, Product, ProductMaterial, ProductTag, MaterialTag


class MaterialInline(admin.TabularInline):
    model = ProductMaterial
    exclude = ['created_at', 'updated_at']
    extra = 1
    raw_id_fields = ['material']


class ProductTagInline(admin.TabularInline):
    model = ProductTag
    exclude = ['created_at', 'updated_at']
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductTagInline, MaterialInline]
    exclude = ['created_at', 'updated_at']
    list_display = ['name', 'sku', 'size', 'tags', 'stock', 'cost']
    list_filter = ['producttag__tag']
    save_as = True

    def tags(self, obj):
        return ', '.join([pt.tag for pt in obj.producttag_set.all()])

    def cost(self, obj):
        return f"{obj.compute_cost():.2f}"


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
    list_display = ['name', 'sku', 'size', 'tags', 'price_per_p', 'units_per_p', 'stock_uf', 'vendor_link']
    list_filter = ['materialtag__tag']
    save_as = True

    def price_per_p(self, obj):
        return int_float(obj.price_per_package)

    price_per_p.short_description = 'Price/p'

    def units_per_p(self, obj):
        return int_float(obj.units_per_package)

    units_per_p.short_description = 'Units/p'

    def stock_uf(self, obj):
        return int_float(obj.stock)

    stock_uf.short_description = 'Stock'

    def tags(self, obj):
        return ', '.join([pt.tag for pt in obj.materialtag_set.all()])

    def vendor_link(self, obj):
        if obj.vendor_url:
            return mark_safe(f'<a href="{obj.vendor_url}">{compact_url(obj.vendor_url)}</a>')
        else:
            return None


def compact_url(url):
    prefixes = ['https://', 'http://', 'www.']
    for prefix in prefixes:
        if url.startswith(prefix):
            url = url[len(prefix):]

    while url.endswith('/'):
        url = url[:-1]

    return truncatechars(url, 20)


def int_float(v):
    can_be_int = int(v)
    if can_be_int == v:
        return can_be_int
    return v
