from django.shortcuts import render
from rest_framework import generics


# Create your views here.

class PostDetailView(generics.ListAPIView):
    template_name = "post.html"

    def get(self, request, *args, **kwargs):
        from .models import Post, Comment
        post = Post.objects.get(pk=kwargs['pk'])
        try:
            comments = Comment.objects.get(post=kwargs['pk'])
        except:
            comments = Comment.objects.filter(post=kwargs['pk'])
        args = {
            "title": "Post Detail",
            "permissions": "permissions",
            "app_name": "Forum",
            "post": post,
            "comments": comments,
            "post_id": kwargs['pk']
        }
        return render(request, template_name=self.template_name, context=args)
