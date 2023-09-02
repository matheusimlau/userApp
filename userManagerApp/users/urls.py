from django.urls import path
from users import views

urlpatterns = [
    path("login/", views.LoginUserView, name="Login"),
    path("register/", views.RegisterUserView, name="Register"),
    path("logout/", views.LogoutUserView, name="Logout"),
    path("", views.HomePageView, name="Home"),
]
