from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('accounts/', include("django.contrib.auth.urls")),
    path("accounts/signup/", views.signup, name="signup"),
    path("posts/create/", views.create_post, name="create_post"),
    path("posts/<int:post_id>/", views.view_post, name="view_post"),
    path("posts/<int:post_id>/comment/", views.create_post_comment, name="create_post_comment"),
    path("courses", views.courses, name="courses"),
    path("courses/<int:course_id>/", views.view_course, name="view_course"),
    path("courses/<int:course_id>/lessons/<int:lesson_id>/", views.view_lesson, name="view_lesson"),
    path("courses/<int:course_id>/exercises/<int:exercise_id>/", views.view_exercise, name="view_exercise"),
]