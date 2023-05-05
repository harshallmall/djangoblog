from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts, name='posts'),
    path('posts/<int:pk>/', views.post_details, name='post_details'),
    path('post/new/', views.new_post, name='new_post'),
    path('post/<int:pk>/edit/', views.edit_posts, name='edit_posts'),
    path('drafts/', views.draft_posts, name='draft_posts'),
    path('post/<pk>/publish/', views.publish_posts, name='publish_posts'),
    path('post/<pk>/delete/', views.delete_posts, name='delete_posts'),
    path('post/<int:pk>/comment/', views.post_comments, name='post_comments'),
    path('comment/<int:pk>/approve/', views.approve_comments, name='approve_comments'),
    path('comment/<int:pk>/delete/', views.delete_comments, name='delete_comments'),
]