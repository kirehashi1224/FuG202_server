import  django_filters
from rest_framework import viewsets, filters
from django_filters import rest_framework as filters

from .models import Restaurant, Genre
from .serializer import RestaurantSerializer, GenreSerializer

class RestaurantFilter(filters.FilterSet):
    # フィルタの定義
    name = filters.CharFilter(name="name", lookup_expr='contains')
    address = filters.CharFilter(name="address", lookup_expr='contains')
    class Meta:
        model = Restaurant
        # フィルタを列挙する。
        # デフォルトの検索方法でいいなら、モデルフィールド名のフィルタを直接定義できる。
        fields = ['name', 'address']


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_class = RestaurantFilter

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer