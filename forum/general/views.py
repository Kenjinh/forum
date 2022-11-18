from django.shortcuts import render
from rest_framework import generics
from topics.forms import *
from topics.models import *


# Create your views here.

class HomePageView(generics.ListAPIView):
    template_name = "home.html"
    categories = PostCategory.objects.all()
    form = NewPostForm()

    def get(self, request, *args, **kwargs):
        args = {
            "title": "Home",
            "permissions": "permissions",
            "app_name": "Forum",
            "categories": self.categories,
            "form": self.form
        }
        return render(request, template_name=self.template_name, context=args)
