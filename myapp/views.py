from django.shortcuts import render

from . import models

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html',{})


def blog(request):

    article_list = models.Article.objects.all()
    context = {'article_list': article_list}
    return render(request, 'myapp/blog.html', context)
