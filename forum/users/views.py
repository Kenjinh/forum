from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from rest_framework import generics
from django.contrib import messages
from .forms import NewUserForm


# Create your views here.

class LoginPageView(generics.ListAPIView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        args = {
            "title": "Login",
            "permissions": "permissions",
            "app_name": "Forum"
        }
        return render(request, template_name=self.template_name, context=args)


def RegisterPage(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f"New Account Created: {email}")
            print(user)
            login(request, user)
            messages.info(request, f"You are now logged in as {email}")
            messages.success(request, "Registration successful.")
            return redirect("main:Home Page")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
                messages.error(request, "Unsuccessful registration. Invalid information.")
                form = NewUserForm()
                args = {
                    "title": "Register",
                    "permissions": "permissions",
                    "app_name": "Forum",
                    "form": form,
                    "erro_form": f"{form.error_messages[msg]}"
                }
                return render(request=request, template_name="register.html", context=args)
    form = NewUserForm()
    args = {
        "title": "Register",
        "permissions": "permissions",
        "app_name": "Forum",
        "form": form
    }
    return render(request=request, template_name="register.html", context=args)

