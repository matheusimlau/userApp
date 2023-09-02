from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUSerForm, UserLoginForm


def RegisterUserView(request):
    form = CreateUSerForm()

    if request.method == "POST":
        form = CreateUSerForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, f"Account successfully created for {user}")
            return redirect("Login")

    context = {"form": form}
    return render(request, "register.html", context)


def LoginUserView(request):
    form = UserLoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("Home")
        else:
            messages.info(request, "Username or Password might be incorrect")

    context = {"form": form}
    return render(request, "login.html", context)


def LogoutUserView(request):
    logout(request)
    return redirect("Login")


@login_required(login_url="Login")
def HomePageView(request):
    return render(request=request, template_name="home.html")
