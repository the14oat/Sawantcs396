from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('accounts/', include("django.contrib.auth.urls")),
    path("posts/create/", views.create_post, name="create_post"),
    path("posts/<int:post_id>/", views.view_post, name="view_post"),
    path("posts/<int:post_id>/comment/", views.create_post_comment, name="create_post_comment"),
    path("accounts/signup/", views.signup, name="signup")
]