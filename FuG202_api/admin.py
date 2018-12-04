from django.contrib import admin

from .models import Restaurant, Genre


@admin.register(Restaurant)
class Restaurant(admin.ModelAdmin):
    pass


@admin.register(Genre)
class Genre(admin.ModelAdmin):
    pass
