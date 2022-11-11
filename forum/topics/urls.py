from django.urls import path, re_path
from . import apis
from . import views

urlpatterns = [
    path("api/comment/", apis.CommentController.as_view(), name="Comment-API"),
    path("api/post-category/", apis.PostCategoryController.as_view(), name="PostCategory-API"),
    path("api/post/", apis.PostController.as_view(), name="Post-API"),
    re_path("(?P<pk>\d+)/", views.PostDetailView.as_view(), name="PostDetail")
]