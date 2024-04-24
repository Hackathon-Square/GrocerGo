from django.shortcuts import render, redirect

from .forms import UserRegisterForm, LoginForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

from django.contrib import messages


def homepage(request):
    return render(request, "users/search.html")


@login_required(login_url="login")
def profile(request):
    return render(request, "users/profile.html")


def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        print(form)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            print(form.errors)
            messages.error(request, form.errors)

    contxet = {"form": form}

    return render(request, "users/register.html", context=contxet)


def my_login(request):

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return redirect("login")

    context = {"form": form}

    return render(request, "users/login.html", context=context)


def setting(request):
    pass


def feedback(request):
    pass


def coupon(request):
    pass


def my_logout(request):
    logout(request)
    return redirect("login")
