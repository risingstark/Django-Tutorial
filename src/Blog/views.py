from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .forms import BlogForm
from .models import Article

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
# Create your views here.


# these are based on a Class View
class ArticleListView(ListView):
    template_name = 'article/article_list.html'
    queryset = Article.objects.all()    #<blog>/<modelname>_list.html

class ArticleDetailView(DetailView):
    template_name = 'article/article_detail.html'
    # queryset = Article.objects.all()    #<blog>/<modelname>_detail.html

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

# these are functions based view
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
