from django.shortcuts import render

# Create your views here.
def categories(requests):
    return render(request=requests, template_name='categories.html')
