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

# generate a course model with the following attributes: instructor, code, name, exercises, and lessons

class Course(models.Model):
    # Model Attributes
    code = models.CharField(max_length= 255)
    name = models.CharField(max_length= 255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    students = models.ManyToManyField(Profile, related_name="courses")

    # Foreign Keys
    instructor = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Lesson(models.Model):
    # Model Attributes
    name = models.CharField(max_length= 255)
    description = models.TextField()
    body = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # Foreign Keys
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)