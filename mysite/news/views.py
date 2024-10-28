from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category


def index(request):
    news = News.objects.all()
    category = Category.objects.all()
    # news = News.objects.order_by("-created_at")
    mycontext = {
        'news': news,
        'category': category,
        'title': "List of locations"
    }
    return render(request, template_name="news/index.html", context=mycontext)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.get(pk=category_id)
    category = Category.objects.all()
    mycontext = {
        'news': news,
        'categories': categories,
        'category': category,
    }
    return render(request, template_name="news/category.html", context=mycontext)



def test(request):
    return HttpResponse('<h1>Test page</h1>')