from django.urls import path
from . import views
from . import apis
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="login.html"),                              name="Login"),
    path('register/', views.RegisterPage,                                                              name="Register"),
    path('logout/', auth_views.LogoutView.as_view(),                                                     name="Logout"),
    path('profile/', views.ProfilePageView.as_view(),                                                   name="Profile"),
    path('api/profile/', apis.ProfileAPI.as_view(),                                                         name="Profile-API"),
]