from django.shortcuts import render, redirect
from rest_framework import generics
from .forms import *


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


class CategoryDetailView(generics.ListAPIView):
    template_name = "category.html"
    form = NewCategoryForm()

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            args = {
                "title": "Category Detail",
                "permissions": "permissions",
                "app_name": "Forum",
                "form": self.form,
            }
            return render(request, template_name=self.template_name, context=args)
        else:
            return redirect("/")

    def post(self, request, *args, **kwargs):
        from .models import PostCategory
        if request.user.is_staff:
            form = NewCategoryForm(request.POST)
            if form.is_valid():
                category = PostCategory(category=form.cleaned_data['category'])
                category.save()
                return redirect("/topics/categories/")
            else:
                return redirect("/topics/categories/")
        else:
            return redirect("/")