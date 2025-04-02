from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Post, Comment
from .forms import ProfileUpdateForm
from datetime import datetime

# Create your views here.


class HomeView(generic.ListView):
    template_name = "securityforum/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all()


class PostView(generic.DetailView):
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


def add_comment(request):
    data = request.POST
    content = data["content"]
    post_id = data["post_id"]
    post = Post.objects.get(id=post_id)
    author = request.user
    new_comment = Comment(content=content, author=author, post=post)
    new_comment.save()
    return HttpResponseRedirect(reverse("securityforum:post", args=(post_id,)))


def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("securityforum:home", args=(request.user.profile,)))
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'securityforum/update_profile.html', {'form': form})
