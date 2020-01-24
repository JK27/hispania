from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import LoginForm

# --------------------------------------------------------- Index view


def index(request):
    return render(request, "index.html")

# --------------------------------------------------------- Login view


def login_user(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have succesfully logged in.")
            else:
                login_form.add_error(None, "Your username of password is incorrect.")
    else:
        login_form = LoginForm()

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
    auth.logout(request)
    messages.success(request, "You have succesfully been logged out.")
    return redirect(reverse('index'))
