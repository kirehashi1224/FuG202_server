from django.contrib import admin

from .models import Restaurant, PriceTag, GenreTag, DistanceTag


@admin.register(Restaurant)
class Restaurant(admin.ModelAdmin):
    pass


@admin.register(PriceTag)
class Tag(admin.ModelAdmin):
    pass


@admin.register(GenreTag)
class Tag(admin.ModelAdmin):
    pass


@admin.register(DistanceTag)
class Tag(admin.ModelAdmin):
    pass
