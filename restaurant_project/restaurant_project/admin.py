from django.contrib import admin
from .models import Category, Dish


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "available", "category")
    list_filter = ("available", "category")
    search_fields = ("name",)
    list_editable = ("price", "available")