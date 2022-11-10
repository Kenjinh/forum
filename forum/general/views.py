from django.shortcuts import render
from rest_framework import generics

from topics.models import *

# Create your views here.

class HomePageView(generics.ListAPIView):
    template_name = "home.html"
    categories = list(PostCategory.objects.values_list('id', 'category'))
    def get(self, request, *args, **kwargs):
        args = {
            "title": "Home",
            "permissions": "permissions",
            "app_name": "Forum",
            "categories": self.categories
        }
        return render(request, template_name=self.template_name, context=args)

