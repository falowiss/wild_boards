from django.db import models

class Category(models.Model):
    """Категория блюда/напитка"""
    name = models.CharField(max_length=100, verbose_name="Название")
    icon = models.CharField(max_length=50, verbose_name="Иконка", blank=True)
    order = models.IntegerField(default=0, verbose_name="Порядок")
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['order']
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    """Пункт меню"""
    CATEGORY_TYPES = [
        ('food', 'Еда'),
        ('drink', 'Напиток'),
        ('other', 'Другое'),
    ]
    
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    item_type = models.CharField(max_length=10, choices=CATEGORY_TYPES, default='food', verbose_name="Тип")
    is_popular = models.BooleanField(default=False, verbose_name="Популярное")
    is_vegetarian = models.BooleanField(default=False, verbose_name="Вегетарианское")
    order = models.IntegerField(default=0, verbose_name="Порядок")
    
    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.price} руб."

class Contact(models.Model):
    """Контактная информация"""
    company_name = models.CharField(max_length=200, verbose_name="Название компании")
    address = models.TextField(verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email", blank=True)
    working_hours = models.CharField(max_length=100, verbose_name="Часы работы")
    map_url = models.URLField(verbose_name="Ссылка на карту", blank=True)
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
    
    def __str__(self):
        return self.company_name
    
