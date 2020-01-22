from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout
from django.contrib import messages
from accounts.forms import LoginForm

# --------------------------------------------------------- Index view


def index(request):
    return render(request, "index.html")

# --------------------------------------------------------- Login view


def login_user(request):
    login_form = LoginForm
    return render(request, 'login.html', {"login_form": login_form})
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)

    # if user is not None:
    #     login(request, user)
    #     # Redirect to success page (i.e. profile page)
    # else:
    #     # Return invalid login error message

# --------------------------------------------------------- Logout view


def logout_user(request):
    logout(request)
    messages.success(request, "You have succesfully been logged out.")
    return redirect(reverse('index'))
