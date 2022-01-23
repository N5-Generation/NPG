from django.urls import path

from . import views

urlpatterns = [
    path('add-social', views.SocialCreationView.as_view(), name='form'),
    path('', views.social_admin, name='social_admin'),
]
