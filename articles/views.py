from django.shortcuts import render, get_object_or_404
from .models import Article

def view_article(request, article_id):
    retrieved_article = get_object_or_404(Article, id=article_id)
    # SELECT * FROM Articles where article.id = article_id;

    context = {
        "article": retrieved_article,
        "test": "Lorem ipsum",
    }

    return render(request, 'articles/article.html', context)

def home(request):
    articles = Article.objects.all()

    context = {
        "articles": articles,
    }

    return render(request, 'articles/index.html', context)