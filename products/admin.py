from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class Product_imageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product_image._meta.fields]

    class Meta:
        model = Product_image


admin.site.register(Product_image, Product_imageAdmin)

