from django.shortcuts import render, redirect
from .models import Blog, Comments
from django.shortcuts import get_object_or_404
from .forms import CommentForm


def blog_list(request):
    posts = Blog.objects.all()

    # Last 4 posts for carousel in base.html
    carousel = Blog.objects.all().order_by("-id")[:4]
    return render(request, "list.html", {"posts": posts, "carousel": carousel})


def blog_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    comments = post.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect("detail", pk=pk)
    else:
        form = CommentForm()
    return render(
        request, "detail.html", {"post": post, "form": form, "comments": comments}
    )
