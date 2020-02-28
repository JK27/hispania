from django.contrib.auth.models import User
from django.db.models import Q


class EmailAuth:
    # Authenticate user by email and password

    def authenticate(self, username_or_email=None, password=None):
        # Get insatance of User based on email and verify password

        users = User.objects.filter(Q(username__iexact=username_or_email) |
                                    Q(email__iexact=username_or_email))

        if not users:
            return None

        user = users[0]

        if user.check_password(password):
            return user

        return None

    def get_user(self, user_id):
        # Used by Django auth system to retrieve user instance

        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            return None

        except User.DoesNotExist:
            return None
