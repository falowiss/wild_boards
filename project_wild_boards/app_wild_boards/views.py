from django.shortcuts import render
from .models import MenuItem, Category, Contact

def home(request):
    """Главная страница"""
    # Получаем популярные блюда и напитки
    popular_food = MenuItem.objects.filter(is_popular=True, item_type='food')[:3]
    popular_drinks = MenuItem.objects.filter(is_popular=True, item_type='drink')[:3]
    
    # Особенности для УТП
    features = [
        {"title": "Сочное мясо", "subtitle": "с видом на горы", "icon": "mountain"},
        {"title": "Согревающие напитки", "subtitle": "после активного дня", "icon": "fire"},
        {"title": "Апрески", "subtitle": "в атмосфере уюта", "icon": "ski"}
    ]
    
    # Контактная информация
    try:
        contact_info = Contact.objects.first()
    except:
        contact_info = None
    
    context = {
        'title': 'Дикие Доски - Бургерная на высоте 1460м',
        'slogan': 'Дикая бургерная на высоте 1460м',
        'features': features,
        'popular_food': popular_food,
        'popular_drinks': popular_drinks,
        'contact_info': contact_info,
    }
    return render(request, 'app_wild_boards/home.html', context)

def menu(request):
    """Страница меню"""
    # Группируем меню по категориям
    categories = Category.objects.all().prefetch_related('menuitem_set')
    
    # Разделяем на еду и напитки
    food_categories = categories.filter(menuitem__item_type='food').distinct()
    drink_categories = categories.filter(menuitem__item_type='drink').distinct()
    
    context = {
        'title': 'Меню - Дикие Доски',
        'food_categories': food_categories,
        'drink_categories': drink_categories,
    }
    return render(request, 'app_wild_boards/menu.html', context)

def contacts(request):
    """Страница контактов"""
    try:
        contact_info = Contact.objects.first()
    except:
        contact_info = None
    
    context = {
        'title': 'Контакты - Дикие Доски',
        'contact_info': contact_info,
    }
    return render(request, 'app_wild_boards/contacts.html', context)

def about(request):
    """О нас"""
    context = {
        'title': 'О нас - Дикие Доски',
    }
    return render(request, 'app_wild_boards/about.html', context)


