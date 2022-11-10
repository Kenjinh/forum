from django.urls import path
from . import apis

urlpatterns = [
    path("api/comment/", apis.CommentController.as_view(), name="Comment-API"),
]