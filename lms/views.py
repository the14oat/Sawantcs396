from django.shortcuts import render, redirect
from .models import *

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