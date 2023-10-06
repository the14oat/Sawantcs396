from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

# ==========================
# cslearning.com/
# ==========================

def index(request):

    if not request.user.is_authenticated:
        return redirect("login")

    # get all posts
    posts = Post.objects.all().order_by("-created_date")

    context = {
        "posts": posts
    }

    return render(request, "pages/index.html", context)

# ==========================
# cslearning.com/posts/create
# ==========================

def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)

        if (form.is_valid()):
            author = request.user

            created_post = form.save(commit=False)
            created_post.author = author
            created_post.save()

            return redirect("index")

    form = CreatePostForm()
    context = {
        "form": form
    }

    return render(request, "pages/posts/create_post.html", context)