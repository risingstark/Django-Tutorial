from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, *kwargs
    print(request, args,kwargs)
    return HttpResponse("<h1> welcome! </h1>") #string of HTML code

def contact_view(request, *args, **kwargs): # *args, *kwargs
    return HttpResponse("<h1> contact page </h1>") #string of HTML code

def list_view(request, *args, **kwargs): # *args, *kwargs
    return HttpResponse("<h1> list page </h1>") #string of HTML code
