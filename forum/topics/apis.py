from rest_framework.generics import *
from .serializers import *
from .models import *
import datetime

# Create your APIS here.

class CommentController(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.publish_date = datetime.datetime.now()
        serializer.save()
        return super().perform_create(serializer)

class PostCategoryController(ListCreateAPIView):
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer

    def perform_create(self, serializer):
        serializer.save()
        return super().perform_create(serializer)

class PostController(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.publish_date = datetime.datetime.now()
        serializer.save()
        return super().perform_create(serializer)