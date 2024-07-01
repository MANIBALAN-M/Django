from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    hi_title = 'this is django'
    posts = [
        {'title':'post1','content':'content of post 1'},
        {'title':'post2','content':'content of post 1'},
        {'title':'post3','content':'content of post 1'},
        {'title':'post4','content':'content of post 1'}
    ]
    return render(request, 'index.html',{"hi_title": hi_title,"posts": posts})

def detail(request, post_id):
    return render(request,'detail.html')

def old_url(request):
    return redirect(reverse("hi:new_url"))

def new_url(request):
    return HttpResponse("this is new url")
    
    
    
    