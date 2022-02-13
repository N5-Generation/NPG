from django.shortcuts import render
from .models import SocialProfile


def index(request):
    social_profiles = list(SocialProfile.objects.all())

    return render(request, "social_page.n5t", {"social_profiles": social_profiles})
