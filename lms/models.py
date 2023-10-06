from django.db import models
from django.contrib.auth.models import AbstractUser

from ckeditor.fields import RichTextField

# Create your models here.

class Profile(AbstractUser):
    pass

class Post(models.Model):
    # Model Attributes
    title = models.CharField(max_length= 255)
    postBody = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # Foreign Keys
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

class PostComment(models.Model):
    # Model Attributes
    commentBody = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # Foreign Keys
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)