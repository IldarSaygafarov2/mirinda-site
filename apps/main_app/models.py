from django.db import models


class News(models.Model):
    """News model."""
    title = models.CharField(verbose_name='Заголовок', max_length=150)
    short_description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(
        verbose_name='Полное описание', null=True)
    slug = models.SlugField(verbose_name='Короткая ссылка')
    preview = models.ImageField(
        verbose_name='Превью', upload_to='news/previews/')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['created_at']


class PointOfSale(models.Model):
    """Point of sale model."""
    market_name = models.CharField(
        verbose_name='Название магазина', max_length=100, unique=True)
    image = models.ImageField(verbose_name='Фото', upload_to='markets/')
    description = models.TextField(
        verbose_name='Уточнение', null=True, blank=True)
    created_at = models.DateTimeField(
        verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return self.market_name

    class Meta:
        verbose_name = 'Точка продажи'
        verbose_name_plural = 'Точки продажи'
        ordering = ['created_at']


class FAQ(models.Model):
    question = models.CharField(verbose_name='Вопрос', max_length=150)
    answer = models.TextField(verbose_name='Ответ')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопросы-ответы'
        verbose_name_plural = 'Вопросы-ответы'


class Product(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=150, unique=True)
    size = models.PositiveIntegerField(verbose_name='Объем', default=0)
    slug = models.SlugField(verbose_name='Короткая ссылка')
    image = models.ImageField(verbose_name='Фото', upload_to='products/')
    short_description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Полное описание')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='products',
                                 verbose_name='Категория')
    created_at = models.DateTimeField(
        verbose_name='Дата добавления', auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class CompanyValue(models.Model):
    title = models.CharField(verbose_name='Заголовок',
                             max_length=150, unique=True)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ценность компании'
        verbose_name_plural = 'Ценности компании'


class Gallery(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to='gallery/')

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлерея'


class UserRequest(models.Model):
    phone_number = models.CharField(
        verbose_name='Номер телефона', max_length=15)
    first_name = models.CharField(verbose_name='Имя', max_length=150)
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name='Дата отправки заявки')

    def __str__(self):
        return f'{self.first_name} {self.phone_number}'

    class Meta:
        verbose_name = 'Заявка пользователя'
        verbose_name_plural = 'Заявки пользователей'


class UserFeedbackNumber(models.Model):
    phone_number = models.CharField(
        verbose_name='Номер телефона', max_length=15)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Номер пользователя для обратной связи'
        verbose_name_plural = 'Номера пользователей для обратной связи'
