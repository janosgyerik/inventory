from django.contrib import admin

from .models import Material, Product, ProductMaterial


class MaterialInline(admin.TabularInline):
    model = ProductMaterial
    exclude = ['created_at', 'updated_at']
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = [MaterialInline]


admin.site.register(Material)
admin.site.register(Product, ProductAdmin)
