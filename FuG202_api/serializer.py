from rest_framework import serializers

from .models import Restaurant, PriceTag, GenreTag, DistanceTag


class PriceTagSerializer(serializers.ModelSerializer):
    restaurants = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = PriceTag
        fields = ('id', 'name', 'restaurants')


class GenreTagSerializer(serializers.ModelSerializer):
    restaurants = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = GenreTag
        fields = ('id', 'name', 'restaurants')


class DistanceTagSerializer(serializers.ModelSerializer):
    restaurants = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = DistanceTag
        fields = ('id', 'name', 'restaurants')


class RestaurantSerializer(serializers.ModelSerializer):
    priceTags = serializers.SlugRelatedField(many=True, queryset=PriceTag.objects.all(), slug_field='name')
    genreTags = serializers.SlugRelatedField(many=True, queryset=GenreTag.objects.all(), slug_field='name')
    distanceTags = serializers.SlugRelatedField(many=True, queryset=DistanceTag.objects.all(), slug_field='name')

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'timespans', 'image', 'priceTags', 'genreTags', 'distanceTags')
