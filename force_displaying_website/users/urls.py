from django.contrib.auth import views as auth_views
from django.urls import path

from users.forms import EmailAuthForm


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', authentication_form=EmailAuthForm), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
]