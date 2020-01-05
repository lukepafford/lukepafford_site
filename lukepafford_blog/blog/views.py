from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from .models import Posts
from .forms import UploadPostForm

# Create your views here.
class HomeView(TemplateView):
    template_name = "_base.html"


class BlogList(View):
    def get(self, request):
        posts = Posts.objects.all()
        return render(request, "blog/blog_list.html", {"posts": posts})


class BlogUpload(View):
    def get(self, request):
        form = UploadPostForm
        return render(request, "blog/blog_upload.html", {"form": form})

    def post(self, request):
        return redirect("blog_list")
