from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import LoginForm, JoinForm

# --------------------------------------------------------- Index view
""" Displays home page (index.html) """


def index(request):
    return render(request, "index.html")


# --------------------------------------------------------- Join in View
""" Manages the Join in form (registration proccess) """


def member_join(request):
    # If user is already logged in, redirect to Home Page
    if request.user.is_authenticated:
        return redirect(reverse('checkout'))

    if request.method == "POST":
        join_form = JoinForm(request.POST)

        if join_form.is_valid():
            join_form.save()
            # Fields used for user authentication
            username = join_form.cleaned_data['username']
            email = join_form.cleaned_data['email']
            password = join_form.cleaned_data['password1']
            user = authenticate(username=username,
                                email=email,
                                password=password)
            login(request=request, user=user)
            messages.info(request, "You have successfully joined in.")
            return redirect(reverse('checkout'))
        else:
            messages.error(request,
                           "We are unable to register your account at this time.")
    else:
        join_form = JoinForm()

    return render(request, 'join.html', {"join_form": join_form})


# --------------------------------------------------------- Login view
""" Manages the Log in form """


def login_member(request):
    if request.user.is_authenticated:
        return redirect(reverse('profile'))

    if request.method == "POST":
        join_form = JoinForm(request.POST)

        if join_form.is_valid():
            join_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have succesfully registered.")
                return redirect(reverse('profile'))
            else:
                messages.error(
                    request, "Unable to register your account at this time.")

    else:
        join_form = JoinForm()

    return render(request, 'join.html',
                  {"join_form": join_form})

# --------------------------------------------------------- Member Profile View


@login_required    # User must be logged in before being able to see Profile
def member_profile(request):
    user = User.objects.get(username=request.user.username)
    return render(request, 'profile.html', {"profile": user})

# --------------------------------------------------------- Logout view


@login_required     # User must be logged in before being able to log out
def logout_member(request):
    # When user logs out, display success message and redirect to Home Page
    auth.logout(request)
    messages.success(request, "You have succesfully been logged out.")
    return redirect(reverse('index'))
