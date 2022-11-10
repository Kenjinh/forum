from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name="login.html"),                              name="Login"),
    url(r'^register/$', views.RegisterPage,                                                              name="Register"),
    url(r'^logout/$', auth_views.LogoutView.as_view(),                                                     name="Logout")
]