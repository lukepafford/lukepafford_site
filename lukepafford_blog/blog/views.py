from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from .models import Posts

# Create your views here.
class HomeView(TemplateView):
    template_name = "_base.html"


class BlogList(View):
    def get(self, request):
        posts = Posts.objects.all()

        return render(request, "blog/blog_list.html", {"posts": posts})
