from django.urls import path

from . import views

app_name = 'dash'  # Add this line to specify the namespace for the dash app

urlpatterns = [
    path("", views.dash_view, name="index")
]