from django.shortcuts import render

# Create your views here.
from . import models


def index(request):
    return render(request,
                  'blog/index.html')


def blogs_index(request):
    articles = models.Article.objects.all()
    return render(request,
                  'blog/blogs_index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,
                  'blog/article_page.html', {'article': article})

