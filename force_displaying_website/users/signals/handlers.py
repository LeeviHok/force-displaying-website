from django.contrib.auth.signals import user_logged_out
from django.contrib import messages


def logout_message(sender, user, request, **kwargs):
    messages.info(request, 'You have been logged out.')


user_logged_out.connect(logout_message)

