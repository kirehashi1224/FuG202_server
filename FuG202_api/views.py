import  django_filters
from rest_framework import viewsets, filters

from .models import Restaurant, Genre
from .serializer import RestaurantSerializer, GenreSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_fields = ('name', 'address')

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer