from django.urls import path
from .views import HomeView, BlogList, BlogUpload

urlpatterns = [
    path("", BlogList.as_view(), name="blog_list"),
    path("upload", BlogUpload.as_view(), name="blog_upload"),
]
