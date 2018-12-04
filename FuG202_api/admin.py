from django.contrib import admin

from .models import Restaurant, Tag


@admin.register(Restaurant)
class Restaurant(admin.ModelAdmin):
    pass


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    pass
