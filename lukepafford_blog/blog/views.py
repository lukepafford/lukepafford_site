from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Posts
from .forms import UploadPostForm
from .markdown_parser import parse_yaml_post

# Create your views here.
class HomeView(TemplateView):
    template_name = "_base.html"


class PostList(View):
    def get(self, request):
        posts = Posts.objects.all()
        return render(request, "posts/post_list.html", {"posts": posts})


class PostDetail(View):
    def get(self, request, post_id):
        post = get_object_or_404(Posts, pk=post_id)
        return render(request, "posts/post_detail.html", {"post": post})


class PostUpload(LoginRequiredMixin, View):
    def get(self, request):
        form = UploadPostForm
        return render(request, "posts/post_upload.html", {"form": form})

    def post(self, request):
        form = UploadPostForm(request.POST, request.FILES)
        if form.is_valid():
            parsed_data = parse_yaml_post(form.cleaned_data["file"])
            post = Posts()
            post.title = parsed_data["title"]
            post.body = parsed_data["body"]
            post.author = request.user
            post.save()
        return redirect("post_list")
