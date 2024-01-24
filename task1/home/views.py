from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    peoples = [
        {'name': 'vipul', 'age': 20},
        {'name': 'kva', 'age': 19},
        {'name': 'va', 'age': 18},
        {'name': 'abc', 'age': 17}
    ]
    return render(request, "index.html", context={'peoples': peoples})



def success_page(request):
    return HttpResponse("<h1>this is done</h1>")
