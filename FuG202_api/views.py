import  django_filters
import random
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.views import APIView


from .models import Restaurant, Genre, Tag
from .serializer import RestaurantSerializer, GenreSerializer, TagSerializer


class RestaurantFilter(filters.FilterSet):
    # フィルタの定義
    name = filters.CharFilter(name="name", lookup_expr='contains')
    address = filters.CharFilter(name="address", lookup_expr='contains')
    tags = filters.ModelMultipleChoiceFilter(
        name="tags",
        queryset=Tag.objects.all(),
        to_field_name='id',
        conjoined=True,
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
        fields = ['name', 'address', 'id', 'random_extract', 'tags']


class TagFilter(filters.FilterSet):
    tag_name = filters.CharFilter(name="tag_name", lookup_expr='contains')

    class Meta:
        model = Tag
        fields = ['tag_name']


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = RestaurantFilter


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_class = TagFilter
