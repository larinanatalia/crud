from django.contrib import admin

# Register your models here.
from logistic.models import Product, Stock

class StockInline(admin.TabularInline):
    model = Stock.products.through
    extra = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    inlines = [StockInline]

