from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .forms import ProductForm, RawProductForm
from .models import Product

# Create your views here.
def product_list_view(request):
    #list all product objects
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html",context)

def product_delete_view(request,id):
    obj = Product.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html",context)

def dynamic_lookup_view(request, id):
    #obj = Product.objects.get(id=id)
    #obj = get_object_or_404(Product, id=id)
    # this is simple way to handle excption, page404
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404

    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html",context)

# def product_create_view(request):
#     my_form = RawProductForm() #default = request.GET
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             #now data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form" : my_form
#     }
#     return render(request, "products/product_create.html",context)

def product_create_view(request):

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html",context)

def product_detail_view(request, id):

    obj = Product.objects.get(id=id)
    # context = {
    #     "title" : obj.title,
    #     "description": obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html",context)
