from django import template

from news.models import Category

register = template.Library() #регистрируем библиотеку шаблона

@register.simple_tag()
def get_categories():
    return Category.objects.all()