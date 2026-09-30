from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post 
from django.db.models import Q

# Create your views here.
def home(request):

    query = request.GET.get('q', '')

    posts = Post.objects.all().order_by('-created_at')

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__icontains=query)
        )

    return render(
        request,
        'index.html',
        {
            'posts': posts,
            'query': query
        }
    )

def create_post(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')

        Post.objects.create(
            title=title,
            author=author,
            content=content
        )

        messages.success(request, 'Post created successfully!')

        return redirect('home')

    return render(request, 'create_post.html')

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':

        post.title = request.POST.get('title')
        post.author = request.POST.get('author')
        post.content = request.POST.get('content')

        post.save()

        messages.success(request, 'Post updated successfully!')

        return redirect('post_detail', post_id=post.id)

    return render(
        request,
        'edit_post.html',
        {'post': post}
    )

def delete_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('home')

    return redirect('post_detail', post_id=post.id)

def search_posts_api(request):
    query = request.GET.get('q', '')

    posts = Post.objects.all().order_by('-created_at')

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__icontains=query)
        )

    data = [
        {
            'id': post.id,
            'title': post.title,
            'author': post.author,
            'content': post.content[:150],
            'created_at': post.created_at.strftime('%b %d, %Y'),
        }
        for post in posts
    ]

    return JsonResponse(data, safe=False)