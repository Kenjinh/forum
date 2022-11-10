from django.shortcuts import render
from rest_framework import generics

# Create your views here.

class HomePageView(generics.ListAPIView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        args = {
            "title": "Home",
            "permissions": "permissions",
            "app_name": "Forum",
        }
        return render(request, template_name=self.template_name, context=args)

