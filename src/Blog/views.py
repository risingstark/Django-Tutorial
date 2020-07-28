from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .forms import BlogForm
from .models import Article

# Create your views here.
def article_list_view(request):
    #list all article objects
    queryset = Article.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "article/article_list.html",context)

def article_detail_view(request,id):

    obj = Article.objects.get(id=id)
    # context = {
    #     "title" : obj.title,
    #     "description": obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "article/article_detail.html",context)