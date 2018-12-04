from rest_framework import serializers

from .models import Restaurant, Genre, Tag


class TagSerializer(serializers.ModelSerializer):
    restaurants = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = Tag
        fields = ('id', 'tag_name', 'restaurants')


class RestaurantSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, queryset=Tag.objects.all(), slug_field='tag_name')

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'timespans', 'image', 'tags')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'restaurant_id')
