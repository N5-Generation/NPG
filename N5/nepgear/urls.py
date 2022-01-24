from django.urls import path

from . import views

urlpatterns = [
    path("add-social", views.SocialCreationView.as_view(), name="form"),
    path("social-admin", views.social_admin, name="social_admin"),
    path("", views.temp_dash, name="nepgear_dashboard")
]
