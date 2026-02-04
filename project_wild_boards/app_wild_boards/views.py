from django.shortcuts import render

def home(request):
    """Главная страница"""
    return render(request, 'app_wild_boards/home.html', {
        'title': 'Дикие Доски - Бургерная на высоте 1460м'
    })

def menu(request):
    """Страница меню"""
    return render(request, 'app_wild_boards/menu.html', {
        'title': 'Меню - Дикие Доски'
    })

def contacts(request):
    """Страница контактов"""
    return render(request, 'app_wild_boards/contacts.html', {
        'title': 'Контакты - Дикие Доски'
    })

def about(request):
    """О нас"""
    return render(request, 'app_wild_boards/about.html', {
        'title': 'О нас - Дикие Доски'
    })