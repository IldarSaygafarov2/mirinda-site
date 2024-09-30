from rest_framework import generics

from .models import (
    News,
    PointOfSale,
    FAQ,
    Product,
    CompanyValue,
    Gallery
)
from .serializers import (
    NewsListSerializer,
    NewsDetailSerializer,
    PointOfSaleSerializer,
    FAQSerializer,
    ProductSerializer,
    CompanyValueSerializer,
    GallerySerializer
)


class NewsList(generics.ListAPIView):
    """Get list of news objects from DB."""
    queryset = News.objects.all()
    serializer_class = NewsListSerializer


class NewsDetail(generics.RetrieveAPIView):
    """Get one instance of news object from DB by slug field."""
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


class PointOfSaleList(generics.ListAPIView):
    queryset = PointOfSale.objects.all()
    serializer_class = PointOfSaleSerializer


class FAQList(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


class CompanyValueList(generics.ListAPIView):
    queryset = CompanyValue.objects.all()
    serializer_class = CompanyValueSerializer


class GalleryList(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer