from django.urls import path
from django.contrib.auth import views as auth_views
from .views import member_join, member_profile, login_member, logout_member

urlpatterns = [
    path('join/', member_join, name="join"),
    path('profile/', member_profile, name="profile"),
    path('login/', login_member, name="login"),
    path('logout/', logout_member, name="logout"),
    path('password-change/', auth_views.PasswordChangeView.as_view(),
         name="password_change"),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(),
         name="password_change_done"),
    path('password-reset/', auth_views.PasswordResetView.as_view(),
         name="password_reset"),
    path('password-reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
]
