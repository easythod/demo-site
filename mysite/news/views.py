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
        'title': "Список новостей"
    }
    return render(request, template_name="news/index.html", context=mycontext)


def test(request):
    return HttpResponse('<h1>Test page</h1>')