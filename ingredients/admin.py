from django.contrib import admin
from .models import Category, Ingredient

# Admin 
admin.site.register(Category)
admin.site.register(Ingredient)