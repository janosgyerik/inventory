from django.contrib import admin

from .models import Material, Product, ProductMaterial


class MaterialInline(admin.TabularInline):
    model = ProductMaterial
    exclude = ['created_at', 'updated_at']
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = [MaterialInline]


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


class MaterialAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


admin.site.register(Material, MaterialAdmin)
admin.site.register(Product, ProductAdmin)
