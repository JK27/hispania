from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import LoginForm, JoinForm

# --------------------------------------------------------- Index view


def index(request):
    return render(request, "index.html")


# --------------------------------------------------------- Join in View


def member_join(request):
    # If user is already logged in, redirect to Home Page
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        join_form = JoinForm(request.POST)

        if join_form.is_valid():
            join_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully joined in.")
            else:
                messages.error(
                    request, "We are unable to register your account at this time.")
    else:
        join_form = JoinForm()
    return render(request, 'join.html', {"join_form": join_form})

# --------------------------------------------------------- Login view


def login_member(request):
    # Once user is logged in, redirect to Home Page ('index')
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        login_form = LoginForm(request.POST)

        # Validate username and password
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            # If login details are correct, display success message and redirect to Home Page
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Welcome back!")
                return redirect(reverse('profile'))
            # If login is incorrect, display error message
            else:
                login_form.add_error(
                    None, "Your username of password is incorrect.")
    else:
        login_form = LoginForm()

    return render(request, 'login.html', {"login_form": login_form})

# --------------------------------------------------------- Logout view


@login_required     # User must be logged in before being able to log out
def logout_member(request):
    # When user logs out, display success message and redirect to Home Page
    auth.logout(request)
    messages.success(request, "You have succesfully been logged out.")
    return redirect(reverse('index'))


# --------------------------------------------------------- Member Profile View


def member_profile(request):
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})
