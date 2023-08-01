from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','slug',)

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display=('title','slug',)
