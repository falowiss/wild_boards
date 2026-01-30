from django.contrib import admin
from .models import Category, MenuItem, Contact

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'order')
    list_editable = ('order',)
    ordering = ('order',)
    search_fields = ('name',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'item_type', 'is_popular', 'order')
    list_filter = ('item_type', 'category', 'is_popular', 'is_vegetarian')
    list_editable = ('price', 'order', 'is_popular')
    search_fields = ('name', 'description')
    ordering = ('order', 'name')
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'price', 'category', 'item_type')
        }),
        ('Дополнительно', {
            'fields': ('is_popular', 'is_vegetarian', 'order'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'phone', 'email')
    fieldsets = (
        ('Контактная информация', {
            'fields': ('company_name', 'address', 'phone', 'email', 'working_hours')
        }),
        ('Карта', {
            'fields': ('map_url',),
            'classes': ('collapse',)
        }),
    )
