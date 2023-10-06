from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import *

class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'postBody']

class CreatePostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['commentBody']