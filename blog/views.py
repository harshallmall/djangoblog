from django.shortcuts import render
from .models import Post
from django.utils import timezone

def posts(request):
    post = Post.objects.filter(date_posted__lte=timezone.now()).order_by('date_posted')
    return render(request, 'blog/posts.html', {'post': post})
