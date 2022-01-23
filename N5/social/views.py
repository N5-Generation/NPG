from django.shortcuts import render
from .models import SocialProfile


def index(request):

    social_profiles = list(SocialProfile.objects.all())

    return render(request, "test.html", {"nik": social_profiles})
