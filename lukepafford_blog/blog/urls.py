from django.urls import path
from .views import HomeView, BlogList

urlpatterns = [
    path("", BlogList.as_view(), name="blog_list"),
]
