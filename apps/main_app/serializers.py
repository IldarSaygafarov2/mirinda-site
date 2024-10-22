from rest_framework import serializers

from .models import (
    News,
    PointOfSale,
    FAQ,
    Category,
    Product,
    CompanyValue,
    Gallery,
    UserRequest,
    UserFeedbackNumber
)


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['pk', 'title', 'short_description', 'preview']


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['pk', 'title', 'short_description',
                  'full_description', 'preview']


class PointOfSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointOfSale
        fields = ['pk', 'market_name', 'description', 'image']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['pk', 'question', 'answer']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = ['pk', 'name', 'size', 'short_description',
                  'full_description', 'image', 'category']


class CompanyValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyValue
        fields = ['pk', 'title', 'description']


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['pk', 'image']


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = ['pk', 'first_name', 'phone_number']


class UserFeedbackNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFeedbackNumber
        fields = ['pk', 'phone_number']
