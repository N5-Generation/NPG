from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'nepgear'

urlpatterns = [
    path("add-social", views.SocialCreationView.as_view(), name="social_creation"),
    path("social-admin", views.social_admin, name="social_admin"),
    url(r'^delete/(?P<card>[0-9]+)/$', views.social_delete, name='social_delete'),
    path("", views.temp_dash, name="nepgear_dashboard"),
]
