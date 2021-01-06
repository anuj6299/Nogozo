from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Trending, Homec, Homel
from mainapp.forms import FeedbackForm, MerchantFeedbackForm

def index(request):
    all_articles = Article.objects.all().order_by("article_id").reverse()
    variable = 'NOGOZO | Entertainment'
    seoimage = 'https://raw.githubusercontent.com/anuj6299/ecomfiles/master/nogozopreview.jpg'
    seodescription = "India's First Local Market E-Commerce Company"
    seotitle = 'NOGOZO | Entertainment'
    trending = Trending.objects.all().reverse()
    homel = Homel.objects.all().reverse()
    homec = Homec.objects.all().reverse()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()
    context = {
        'all_articles' : all_articles,
        'variable' : variable,
        'seoimage' : seoimage,
        'seodescription' : seodescription,
        'seotitle' : seotitle,
        'trending' : trending,
        'homec' : homec,
        'homel' : homel,
        'form' : form,
     }
    return render(request, 'blog/index.html', context)

def article(request, article_id):
    article = Article.objects.get(article_id=article_id)
    trending = Trending.objects.all()
    variable = article.article_title+' | NOGOZO'
    seoimage = article.article_logo
    seodescription = article.article_summary
    seotitle = article.article_title
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()

    if article.article_id == 1:
        nid = 7
        pid = 6
    elif article.article_id == 2:
        nid = 9
        pid = 8
    else:
        nid = article.article_id -1
        pid = article.article_id -2
    next_article = Article.objects.get(article_id = nid)
    previous_article = Article.objects.get(article_id = pid)

    context = {
        'article' : article,
        'variable' : variable,
        'seoimage' : seoimage,
        'seodescription' : seodescription,
        'seotitle' : seotitle,
        'previous_article': previous_article,
        'next_article': next_article,
        'trending' : trending,
        'form' : form,
     }
    return render(request, 'blog/article.html', context)


