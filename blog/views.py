from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

def posts(request):
    post = Post.objects.filter(date_posted__lte=timezone.now()).order_by('date_posted')
    return render(request, 'blog/posts.html', {'post': post})

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_details.html', {'post': post})

@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.date_posted = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/edit_posts.html', {'form': form})

@login_required
def edit_posts(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_posts.html', {'form': form})

@login_required
def draft_posts(request):
    # The queryset ensures that only posts without published dates are gathered and ordered by their created dates.
    posts = Post.objects.filter(date_posted__isnull=True).order_by('date_created')
    return render(request, 'blog/draft_posts.html', {'posts': posts})

@login_required
def publish_posts(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_details', pk=pk)

@login_required
def delete_posts(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # All Models in Django can be deleted by the .delete() method.
    post.delete()
    # After a post is deleted, the user gets redirected back to all posts.
    return redirect('posts')

def post_comments(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_comments.html', {'form': form})

@login_required
def approve_comments(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_details', pk=comment.post.pk)

@login_required
def delete_comments(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_details', pk=comment.post.pk)