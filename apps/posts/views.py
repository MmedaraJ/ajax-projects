from django.shortcuts import redirect, render
from .models import Post

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/index.html', context)

def new_post(request):
    Post.objects.create(post=request.POST['post'])
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/post.html', context)