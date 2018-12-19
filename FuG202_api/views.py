import random
from rest_framework import viewsets
from django_filters import rest_framework as filters


from .models import Restaurant, PriceTag, GenreTag, DistanceTag
from .serializer import RestaurantSerializer, PriceTagSerializer, GenreTagSerializer, DistanceTagSerializer


class RestaurantFilter(filters.FilterSet):
    # フィルタの定義
    name = filters.CharFilter(name="name", lookup_expr='contains')
    address = filters.CharFilter(name="address", lookup_expr='contains')
    priceTags = filters.ModelMultipleChoiceFilter(
        name="priceTags",
        queryset=PriceTag.objects.all(),
        to_field_name='id',
        lookup_expr='exact'
    )
    genreTags = filters.ModelMultipleChoiceFilter(
        name="genreTags",
        queryset=GenreTag.objects.all(),
        to_field_name='id',
        lookup_expr='exact'
    )
    distanceTags = filters.ModelMultipleChoiceFilter(
        name="distanceTags",
        queryset=DistanceTag.objects.all(),
        to_field_name='id',
        lookup_expr='exact'
    )
    random_extract = filters.CharFilter(method='filter_random_extract')

    def filter_random_extract(self, qs, name, value):
        try:
            if value == "true":
                qs_len = len(qs)-1
                index = random.randint(0, qs_len)
                return qs[index:index+1]
            else:
                return qs
        except:
            return qs

    class Meta:
        model = Restaurant
        # フィルタを列挙する。
        # デフォルトの検索方法でいいなら、モデルフィールド名のフィルタを直接定義できる。
        fields = ['name', 'address', 'id', 'priceTags', 'genreTags', 'distanceTags', 'random_extract']


class PriceTagFilter(filters.FilterSet):
    name = filters.CharFilter(name="name", lookup_expr='contains')

    class Meta:
        model = PriceTag
        fields = ['name']


class GenreTagFilter(filters.FilterSet):
    name = filters.CharFilter(name="name", lookup_expr='contains')

    class Meta:
        model = GenreTag
        fields = ['name']


class DistanceTagFilter(filters.FilterSet):
    name = filters.CharFilter(name="name", lookup_expr='contains')

    class Meta:
        model = DistanceTag
        fields = ['name']


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = RestaurantFilter


class PriceTagViewSet(viewsets.ModelViewSet):
    queryset = PriceTag.objects.all()
    serializer_class = PriceTagSerializer
    filter_class = PriceTagFilter


class GenreTagViewSet(viewsets.ModelViewSet):
    queryset = GenreTag.objects.all()
    serializer_class = GenreTagSerializer
    filter_class = GenreTagFilter


class DistanceTagViewSet(viewsets.ModelViewSet):
    queryset = DistanceTag.objects.all()
    serializer_class = DistanceTagSerializer
    filter_class = DistanceTagFilter
