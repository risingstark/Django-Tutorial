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
    my_context = { "my_name":"sean kim",
                    "my_number": "01063460625",
                    "my_friends_list":["David","Daniel","Justine","Tomas",123]
    }
    return render(request, "about.html", my_context)

def list_view(request, *args, **kwargs): # *args, *kwargs
    return render(request, "list.html", {})
