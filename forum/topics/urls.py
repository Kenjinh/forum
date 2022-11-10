from django.urls import path
from . import apis

urlpatterns = [
    path("api/comment/", apis.CommentController.as_view(), name="Comment-API"),
    path("api/post-category/", apis.PostCategoryController.as_view(), name="PostCategory-API"),
    path("api/post/", apis.PostController.as_view(), name="Post-API"),
]