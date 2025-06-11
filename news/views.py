from django.shortcuts import render
from news.models import Banner, Article, Category

def home_view(request):
    banners = Banner.objects.all()
    trending_articles = Article.objects.filter(is_trending=True)[:7]
    category_cultures = Category.objects.filter(is_active=True)[:7]
    article_business = Article.objects.filter(is_featured=True)[:7]
    article_lifestyles = Article.objects.filter(is_featured=True)[:2]
    return render(request, 'news/index.html', { 'banners': banners , 'trending_articles': trending_articles , 'category_cultures':category_cultures , 'article_business':article_business , 'article_lifestyles':article_lifestyles})


def article_detail_view(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, "template/news/article_details.html",{'article': article})