from modeltranslation.translator import translator, TranslationOptions

from . import models




class NewsTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'short_description',
        'full_description',
    )


@translator.register(models.PointOfSale)
class PointOfSaleTranslationOptions(TranslationOptions):
    fields = (
        'description'
    )


@translator.register(models.FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = (
        'question',
        'answer'
    )


@translator.register(models.Product)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'short_description',
        'full_description',
    )


@translator.register(models.CompanyValue)
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