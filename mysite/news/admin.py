from django.contrib import admin

# Register your models here.
from .models import News,Category # импортируем модель для регистрации


class  NewsAdmin(admin.ModelAdmin): # создаем класс для конфигурации полей в таблице Новости в админке
    list_display = ('id','title','created_at','updated_at','is_published','category') # столбцы в табл Новости
    list_display_links = ('id','title') # отображать как ссылку
    search_fields = ('title','content') # добление поиска по полям
    list_editable = ('is_published',) # добавляем возможность редактировать поле и указываем само поле.Запятая вконце т.к это кортеж
    list_filter = ('is_published','category',) # фильтр по указанным полям

class  CategoryAdmin(admin.ModelAdmin): # создаем класс для конфигурации полей в таблице Новости в админке
    list_display = ('id','title') # столбцы в табл Категори
    list_display_links = ('id','title') # отображать как ссылку
    search_fields = ('title',) # добление поиска по полям


admin.site.register(News,NewsAdmin) # регистрируем модель News
admin.site.register(Category,CategoryAdmin) # регистрируем модель Category