from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_vew(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")

def base_view(request, *args, **kwargs):
    return render(request, "base.html", {})

def page_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list" : [1, 3, 4, 6]
    }
    return  render(request, "page.html", my_context)
