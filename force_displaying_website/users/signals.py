from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.contrib import messages


def logout_message(sender, user, request, **kwargs):
    messages.info(request, 'You have been logged out.')

def test(sender, **kwargs):
    print('Jee...')


user_logged_out.connect(test)
user_logged_in.connect(test)
