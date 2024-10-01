from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from django.db import models
from modeltranslation.admin import TranslationAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

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

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(ModelAdmin, TranslationAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['created_at']
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }


@admin.register(PointOfSale)
class PointOfSaleAdmin(ModelAdmin, TranslationAdmin):
    list_display = ['pk', 'market_name', 'created_at']
    list_display_links = ['pk', 'market_name']
    list_filter = ['created_at']


@admin.register(FAQ)
class FAQAdmin(ModelAdmin, TranslationAdmin):
    list_display = ['pk', 'question']
    list_display_links = ['pk', 'question']


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['pk', 'name']
    list_display_links = ['pk', 'name']


@admin.register(Product)
class ProductAdmin(ModelAdmin, TranslationAdmin):
    list_display = ['pk', 'name', 'size', 'category', 'created_at']
    list_display_links = ['pk', 'name']
    list_filter = ['created_at', 'category']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CompanyValue)
class CompanyValueAdmin(ModelAdmin, TranslationAdmin):
    list_display = ['pk', 'title']
    list_display_links = ['pk', 'title']


@admin.register(Gallery)
class GalleryAdmin(ModelAdmin):
    pass


@admin.register(UserRequest)
class UserRequestAdmin(ModelAdmin):
    list_display = ['pk', 'first_name', 'phone_number']
    list_display_links = ['pk', 'first_name']
    list_filter = ['created_at']


@admin.register(UserFeedbackNumber)
class UserFeedbackNumberAdmin(ModelAdmin):
    list_display = ['pk', 'phone_number']
    list_display_links = ['pk', 'phone_number']