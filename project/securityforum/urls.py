from django.urls import path

from . import views

app_name = "securityforum"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("posts/<pk>", views.PostView.as_view(), name="post"),
    path("post_form", views.post_form, name="post_form"),
    path("create_post", views.create_post, name="create_post"),
    path("add_comment", views.add_comment, name="add_comment"),
    path("update_profile", views.update_profile, name="update_profile")
]
