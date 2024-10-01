from django.urls import path

from . import views

urlpatterns = [
    path('news/', views.NewsList.as_view()),
    path('news/<slug:slug>/', views.NewsDetail.as_view()),
    path('markets/', views.PointOfSaleList.as_view()),
    path('faqs/', views.FAQList.as_view()),
    path('products/', views.ProductList.as_view()),
    path('products/<slug:slug>/', views.ProductDetail.as_view()),
    path('company/values/', views.CompanyValueList.as_view()),
    path('gallery/', views.GalleryList.as_view()),
    path('request/create/', views.UserRequestCreateView.as_view()),
    path('feedback/create/', views.UserFeedbackNumberCreate.as_view()),
]
