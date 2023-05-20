from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.urls import reverse
from users.form import *
from users.models import User

def index(request):
    form=SignUpForm()
    return render(request, "users/SignUp.html", {"form": form, "login": LoginForm()})

def signup(request):
    if request.method == "GET":
        form=SignUpForm()
        return render(
            request, "users/SignUp.html",
            {"form": form}
        )
    elif request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("index"))
    return redirect(reverse("index"))
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=User.objects.get(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
            else:
                form.add_error(None, "Invalid username or password.")
                return redirect(reverse("index"))
    else:
        form = LoginForm()
        return redirect(reverse("index"))


def logout_view(request):
    logout(request)
    return redirect(reverse("index"))