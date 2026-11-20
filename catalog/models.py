from django.db import models


class Category(models.Model):
    # наименование
    name = models.CharField(max_length=150, verbose_name='Наименование', help_text='Введите наименование категории')
    # описание
    description = models.TextField(verbose_name='Описание', help_text='Введите описание категории', blank=True,
                                   null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    # наименование
    name = models.CharField(max_length=150, verbose_name='Наименование', help_text='Введите наименование продукта')
    # описание
    description = models.TextField(verbose_name='Описание', help_text='Введите описание продукта')
    # изображение
    image = models.ImageField(upload_to='products/image', blank=True, null=True, verbose_name='Изображение',
                              help_text='Загрузите изображение продукта')
    # категория
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    # цена за покупку
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', help_text='Введите цену')
    # дата создания
    created_at = models.DateTimeField(auto_now_add=True)
    # дата последнего изменения
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_at', '-updated_at', 'name', 'category', 'price']

    def __str__(self):
        return self.name
