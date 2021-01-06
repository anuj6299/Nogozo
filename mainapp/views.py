from django.shortcuts import render, get_object_or_404
from .forms import FeedbackForm, MerchantFeedbackForm
from .models import Feedback, MerchantFeedback, Merchant, Category, Sets
from blog.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()
    return render(request, 'mainapp/index.html', {'form': form})


def privacy(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'mainapp/thanks.html', context)
    else:
        form = FeedbackForm()    
    context = {
    }
    return render(request, 'mainapp/privacy.html', {'form': form} )


def tnc(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'mainapp/thanks.html', context)
    else:
        form = FeedbackForm()    
    context = {
    }
    return render(request, 'mainapp/tnc.html', {'form': form} )


def comming(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'mainapp/thanks.html', context)
    else:
        form = FeedbackForm()    
    context = {
    }
    return render(request, 'mainapp/comming.html', {'form': form} )


def download(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()
    return render(request, 'mainapp/download.html', {'form': form})

 
def contact(request): 
    all_articles = Article.objects.all().order_by("article_id").reverse()
    context = {
        'all_articles' : all_articles,
     }
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'mainapp/thanks.html', context)
    else:
        form = FeedbackForm()
    return render(request, 'mainapp/contact.html', {'form': form})

 
def merchantcontact(request):
    all_articles = Article.objects.all().order_by("article_id").reverse()
    context = {
        'all_articles' : all_articles,
     }    
    if request.method == 'POST':
        form = MerchantFeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'mainapp/thanks.html', context)
    else:
        form = MerchantFeedbackForm()
    return render(request, 'mainapp/merchantcontact.html', {'form': form})

# def merchant(request):
#     shop = Merchant.objects.all()
#     context = {
#         'shop' : shop,
#     }
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
 
#         if form.is_valid():
#             form.save()
#             return render(request, 'mainapp/thanks.html', context)
#     else:
#         form = FeedbackForm()    
#     return render(request, 'mainapp/merchant.html', {'form': form}, context )

def merchant(request):
    shop = Merchant.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(shop, 5)
    try:
        shops = paginator.page(page)
    except PageNotAnInteger:
        shops = paginator.page(1)
    except EmptyPage:
        shops = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()
    context = {
        'shop' : shop,
        'form' : form,
        'shops' : shops,
     }
    return render(request, 'mainapp/merchant.html', context)

def music(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()
    context = {
        'form' : form,
     }
    return render(request, 'mainapp/music.html', context)

def quizcat(request):
    all_category = Category.objects.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()
    context = {
        'form' : form,
        'all_category' : all_category
     }
    return render(request, 'mainapp/quizcat.html', context)

def sets(request,category_name):
    category = Category.objects.get(category_name=category_name)
    all_category = Category.objects.all()
    all_set = Sets.objects.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()
    context = {
        'all_category' : all_category,
        'category' : category,    
        'all_set' : all_set,
        'form' : form,
     }
    return render(request, 'mainapp/sets.html', context)
    
def quiz(request,set_id):
    all_category = Category.objects.all()
    set_info = Sets.objects.get(set_id = set_id)
    if set_id == Sets.objects.all().count():
        next_id = 1
    else:
        next_id = set_id+ 1

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()   
    context = {
        'all_category' : all_category,
        'set_info' : set_info, 
        'next_id' : next_id, 
        'form' : form  
    }
    return render(request, 'mainapp/quiz.html', context )