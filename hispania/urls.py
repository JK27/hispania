"""hispania URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import index, member_join, member_profile, login_member, logout_member
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', index, name="index"),
    path('join/', member_join, name="join"),
    path('profile/', member_profile, name="profile"),
    path('login/', login_member, name="login"),
    path('logout/', logout_member, name="logout"),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name="password_change"),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password-reset-confirm/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    ]
