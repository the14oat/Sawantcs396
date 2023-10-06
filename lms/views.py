from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
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

# ========================
# cslearning.com/posts/<id>
# ========================

def view_post(request, post_id):
    
    post = Post.objects.get(id=post_id)
    comments = PostComment.objects.filter(post=post_id)

    createPostCommentForm = CreatePostCommentForm()

    context = {
        "post": post,
        "comments": comments,
        "form": createPostCommentForm
    }

    return render(request, "pages/posts/view_post.html", context)

# ======================
# cslearning.com/posts/1
# ======================

def create_post_comment(request, post_id):
    if request.method == "POST":

        post = Post.objects.get(id=post_id)
        form = CreatePostCommentForm(request.POST)

        if form.is_valid():
            author = request.user

            created_comment = form.save(commit=False)
            created_comment.author = author
            created_comment.post = post

            created_comment.save()

            return redirect("view_post", post_id)
        
# ======================
# cslearning.com/accounts/signup
# ======================

def signup(request):


    if request.method == "POST":


        form = RegistrationForm(request.POST)


        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            form.save()


            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")

    form = RegistrationForm()

    context = {
        "form": form
    }

    return render(request, "registration/signup.html", context)

# ======================
# cslearning.com/courses
# ======================

def courses(request):
    
    # we need to get the courses the belong to the logged in user
    user = request.user
    courses = Course.objects.filter(students=user)    

    context = {
        "courses": courses
    }

    return render(request, "pages/courses/index.html", context)
