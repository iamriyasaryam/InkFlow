from django.shortcuts import render, redirect
from . import models 

# Create your views here.
def home(request):
    posts = models.Post.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})

def create_post(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')

        models.Post.objects.create(
            title=title,
            author=author,
            content=content
        )

        return redirect('home')

    return render(request, 'create_post.html')

def post_detail(request, post_id):
    post = models.Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})