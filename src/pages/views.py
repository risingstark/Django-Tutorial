from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, *kwargs
    print(request, args,kwargs)
    #return HttpResponse("<h1> welcome! </h1>") #string of HTML code
    print(request.user)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs): # *args, *kwargs
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs): # *args, *kwargs
    return render(request, "about.html", {})

def list_view(request, *args, **kwargs): # *args, *kwargs
    return render(request, "list.html", {})
