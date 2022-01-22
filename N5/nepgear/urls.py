from django.urls import path

from . import views

urlpatterns = [
    path('', views.SocialCreationView.as_view(), name='form'),
]
