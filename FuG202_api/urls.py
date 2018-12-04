# coding: utf-8

from rest_framework import routers
from .views import RestaurantViewSet, PriceTagViewSet, GenreTagViewSet, DistanceTagViewSet

router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'price_tags', PriceTagViewSet)
router.register(r'genre_tags', GenreTagViewSet)
router.register(r'distance_tags', DistanceTagViewSet)
