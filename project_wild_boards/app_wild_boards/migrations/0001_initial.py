from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('icon', models.CharField(blank=True, max_length=50, verbose_name='Иконка')),
                ('order', models.IntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200, verbose_name='Название компании')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('working_hours', models.CharField(max_length=100, verbose_name='Часы работы')),
                ('map_url', models.URLField(blank=True, verbose_name='Ссылка на карту')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')),
                ('item_type', models.CharField(choices=[('food', 'Еда'), ('drink', 'Напиток'), ('other', 'Другое')], default='food', max_length=10, verbose_name='Тип')),
                ('is_popular', models.BooleanField(default=False, verbose_name='Популярное')),
                ('is_vegetarian', models.BooleanField(default=False, verbose_name='Вегетарианское')),
                ('order', models.IntegerField(default=0, verbose_name='Порядок')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_wild_boards.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
                'ordering': ['order', 'name'],
            },
        ),
    ]