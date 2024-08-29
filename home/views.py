from django.shortcuts import render, get_object_or_404
from home.models import Article
from home.forms import EmailForm
from django.core.paginator import Paginator


def home(request):
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
    cat = request.GET.get("cat")
    page = request.GET.get("page")
    search = request.GET.get("search")
    article_four = Article.objects.order_by('-id')[:4]
    article_six = Article.objects.order_by('-id')[:6]
    article_game_three = Article.objects.filter(category='game')[:3]
    article_human_three = Article.objects.filter(category='human')[:3]
    all_categories = list(set(Article.objects.values_list('category', flat=True)))

    context = {
        "search": search,
        "cat": cat,
        "page": page,
        "article_four": article_four,
        "article_game_three": article_game_three,
        "article_human_three": article_human_three,
        "article_six": article_six,
        "all_categories": all_categories,
        "form": form
    }
    return render(request=request, template_name='index.html', context=context)
def single_page(request):
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
    cat = request.GET.get("cat")
    article_three = Article.objects.filter(category=cat)
    context = {
        "cat": cat,
        "article_three": article_three,
        "form": form
    }
    return render(request=request, template_name='single.html', context=context)

def categories_page(request):
    cat = request.GET.get("cat")
    all_categories = list(set(Article.objects.values_list('category', flat=True)))

    page = request.GET.get("page")
    paginator = Paginator(Article.objects.filter(category=cat), 2)
    articles = paginator.get_page(page)
    context = {
        "articles": articles,
        "cat": cat,
        "all_categories": all_categories,
        "page": page
    }
    return render(request=request, template_name='categories.html', context=context)



def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    print(article)
    context = {

        "article": article

    }
    return render(request, 'single.html', context=context)


