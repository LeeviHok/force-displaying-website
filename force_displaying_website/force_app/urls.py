from django.urls import path

from force_app import views as force_app_views

urlpatterns = [
    path('', force_app_views.home, name="force_app-home"),
]
