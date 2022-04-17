from django.shortcuts import render
from django.http import HttpResponse #импортируем стандартный модуль
from .models import News,Category  #импортируем модель News

# Create your views here.
# создаем функцию index

def index(request):
    news = News.objects.all() #добавляем функцию вывода новостей и базы данных
    categories = Category.objects.all() #добавляем вывод названий категорий на странице
    return render(request,'news/index.html',{'news':news,'title':'Список новостей','categories':categories})

def  get_category(request,category_id):
    news= News.objects.filter(category_id=category_id)
    categories=Category.objects.all()
    category=Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'categories': categories,'category':category})

def test(request):
    #print(response)
    return HttpResponse('<h1>Тестовая страница</h1>')

def test2(request):
    #print(response)
    return HttpResponse('<h1>Привет,бро</h1>')