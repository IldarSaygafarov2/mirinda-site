from rest_framework import generics

from .models import (
    News,
    PointOfSale,
    FAQ,
    Product,
    CompanyValue,
    Gallery,
    UserRequest,
    UserFeedbackNumber
)

from .serializers import (
    NewsListSerializer,
    NewsDetailSerializer,
    PointOfSaleSerializer,
    FAQSerializer,
    ProductSerializer,
    CompanyValueSerializer,
    GallerySerializer,
    UserRequestSerializer,
    UserFeedbackNumberSerializer
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


class UserRequestCreateView(generics.CreateAPIView):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer


class UserFeedbackNumberCreate(generics.CreateAPIView):
    queryset = UserFeedbackNumber.objects.all()
    serializer_class = UserFeedbackNumberSerializer
