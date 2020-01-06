from django.urls import path
from .views import HomeView, PostList, PostUpload, PostDetail

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("post/<int:post_id>/", PostDetail.as_view(), name="post_detail"),
    path("upload/", PostUpload.as_view(), name="post_upload"),
]
