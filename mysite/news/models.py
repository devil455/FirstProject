from django.db import models

# Создаем класс News(она же таблица)
class News(models.Model):
    title = models.CharField(max_length= 150, verbose_name='Наменование')
    content= models.TextField(blank=True, verbose_name='Контент')
    created_at= models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    updated_at= models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo= models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)# blank означает необязательное поле для заполнения
    is_published=models.BooleanField(default=True,verbose_name='Опубликовано?')
    category= models.ForeignKey('Category', on_delete=models.PROTECT,null=True,verbose_name='Категория') # прописываем связь таблиц через ForeignKey

    def __str__(self):    #метод строкового представления обьекта
        return self.title
# после создания модели необходимо создать и выполнить миграцию python manage.py makemigrations/migrate
    class Meta: # создаем класс Мета для переименования в админке(работает только с админкой)
        verbose_name= 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at'] # сортировка


class Category(models.Model):# создаём новый клас(таблицу) для категорий новостей(первичная модель)
    title = models.CharField(max_length=150, db_index=True,verbose_name='Наименование категории')

    def __str__(self):  # метод строкового представления обьекта (для отображения не Cat. object а по названию категории)
        return self.title

    class Meta: # создаем класс Мета для переименования в админке
        verbose_name= 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title'] # сортировка

