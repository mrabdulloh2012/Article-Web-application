from django.core.paginator import Paginator
from django.shortcuts import render
from home.models import Article  # Import your Article model


def search_page(request):
    cat = request.GET.get("cat")
    search = request.GET.get("search")
    page = request.GET.get("page")

    # Start with a base queryset
    articles_query = Article.objects.all()

    # Apply category filter if provided
    if cat:
        articles_query = articles_query.filter(category=cat)

    # Apply search filter if provided
    if search:
        articles_query = articles_query.filter(title__icontains=search)

    # Set up pagination
    paginator = Paginator(articles_query, 2)
    articles_two = paginator.get_page(page)

    # Get all categories for the context
    all_categories = list(set(Article.objects.values_list('category', flat=True)))

    context = {
        "search": search,
        "articles_two": articles_two,
        "cat": cat,
        "page": page,
        "all_categories": all_categories
    }
    return render(request, 'search.html', context=context)