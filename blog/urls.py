from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('api/search/', views.search_posts_api, name='search_posts_api'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path(
        'post/<int:post_id>/edit/',
        views.edit_post,
        name='edit_post'
    ),
    path(
    'post/<int:post_id>/delete/',
    views.delete_post,
    name='delete_post'
),
]