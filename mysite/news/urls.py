from django.urls import path #импортируем маршруты
from .views import * #импортируем все функции с дериктории news/views


# создаем переменную urlpatterns со списком адресов
urlpatterns =[
    path('',index,name='home'),# пустая строка '' указывает на страницу index
    path('category/<int:category_id>/', get_category,name='category'),# указываем необходимый маршрут
    path('test/',test),
    path('test2',test2)
]