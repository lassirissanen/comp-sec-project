from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Post, User
from datetime import datetime

# Create your views here.


class HomeView(generic.ListView):
    template_name = "securityforum/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all()


class PostView(generic.DeleteView):
    model = Post
    context_object_name = "post"
    template_name = "securityforum/post.html"


def post_form(request):
    return render(request, "securityforum/post_form.html", {})


def create_post(request):
    data = request.POST
    header = data["header"]
    content = data["content"]
    if header == "" or content == "":
        return render(request, "securityforum/post_form.html", {"error_message": "Please give both header and content"})
    author = request.user
    new_post = Post(header=header, content=content,
                    pub_date=datetime.now(), author=author)
    new_post.save()
    return HttpResponseRedirect(reverse("securityforum:post", args=(new_post.id,)))
