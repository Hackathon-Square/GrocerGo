from django.shortcuts import render, redirect

from .forms import UserRegisterForm, LoginForm, FeedbackForm
from .models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .intention import use_gpt
from .process import process_gpt


def homepage(request):
    return render(request, "users/homepage.html")


@login_required(login_url="login")
def profile(request):
    return render(request, "users/profile.html")


def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            ##TODO: registration error not identified
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
                users = User.objects.get(username__contains=username)
                request.session["is_login"] = "true"
                request.session["username"] = username
                request.session["email"] = users.email
                request.session["is_staff"] = users.is_staff
                login(request, user)
                return redirect("homepage")
            else:
                return redirect("login")

    context = {"form": form}

    return render(request, "users/login.html", context=context)


def setting(request):
    pass


def feedback(request):
    form = FeedbackForm()
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = request.POST["feedback"]
            user_email = request.session["email"]
            authority = request.session["is_staff"]
            # feedback as input into GPT
            process_gpt(feedback, user_email, authority)
            return redirect("homepage")
        else:
            ##TODO: feedback error not identified
            messages.error(request, form.errors)

    return render(request, "users/feedback.html", context={"form": form})


def coupon(request):
    username = request.session["username"]
    user = User.objects.get(username=username)
    return render(request, "users/coupon.html", {"user": user})


def my_logout(request):
    logout(request)
    return redirect("login")
