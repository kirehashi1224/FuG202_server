# coding: utf-8

from rest_framework import routers
from .views import RestaurantViewSet, TagViewSet

router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'tags', TagViewSet)
