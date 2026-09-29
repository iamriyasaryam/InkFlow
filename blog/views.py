from django.shortcuts import render, redirect, get_object_or_404
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


def edit_post(request, post_id):
    post = get_object_or_404(models.Post, id=post_id)

    if request.method == 'POST':

        post.title = request.POST.get('title')
        post.author = request.POST.get('author')
        post.content = request.POST.get('content')

        post.save()

        return redirect('post_detail', post_id=post.id)

    return render(
        request,
        'edit_post.html',
        {'post': post}
    )

def delete_post(request, post_id):

    post = get_object_or_404(models.Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return redirect('post_detail', post_id=post.id)