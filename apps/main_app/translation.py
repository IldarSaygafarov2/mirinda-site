from modeltranslation.translator import translator, TranslationOptions

from . import models




class NewsTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'short_description',
        'full_description',
    )


class PointOfSaleTranslationOptions(TranslationOptions):
    fields = (
        'description',
    )


class FAQTranslationOptions(TranslationOptions):
    fields = (
        'question',
        'answer'
    )


class ProductTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'short_description',
        'full_description',
    )


class CompanyValueTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description'
    )


translator.register(models.News, NewsTranslationOptions)
translator.register(models.FAQ, FAQTranslationOptions)
translator.register(models.Product, ProductTranslationOptions)
translator.register(models.CompanyValue, CompanyValueTranslationOptions)
translator.register(models.PointOfSale, PointOfSaleTranslationOptions)