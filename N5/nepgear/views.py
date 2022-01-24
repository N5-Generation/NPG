from pathlib import Path
from django.shortcuts import redirect, render
from django.views import View
from django.utils.decorators import method_decorator
import json
import requests
import os

from NPG.settings.base import STATICFILES_DIRS
from NPG.helpers import ajax_required, get_colors
from .forms import SocialCreationForm, possible_extension
from social.models import SocialProfile

# Create your views here.

@method_decorator(ajax_required, name="get")
class SocialCreationView(View):
    ctx = {
        "form": SocialCreationForm(),
    }

    def get(self, request, *args, **kwargs):
        
        return render(request, "social_creation.html", self.ctx)

    def post(self, request, *args, **kwargs):
        payload = json.loads(request.body.decode())
        form = SocialCreationForm(payload)
        
        if form.is_valid():
            # Quick binds
            social_name = form.cleaned_data["social_name"]
            social_icon = form.cleaned_data["social_icon"]
            file_extention = None

            for extension in possible_extension:
                if extension in social_icon:
                    file_extention = extension 

            icon_download = requests.get(social_icon).content
            icon_save_path = Path.joinpath(STATICFILES_DIRS[0],"social_icons" , f"social_{social_name}{file_extention}")

            if os.path.exists(icon_save_path):
                os.mkdir(Path.joinpath(STATICFILES_DIRS[0],"social_icons"))

            with open(icon_save_path, "wb") as save_icon:
                save_icon.write(icon_download)

            icon_main_color = get_colors(icon_save_path)[0]

            instance = form.save(commit=False)
            
            if icon_main_color is not None:
                instance.social_color = str(icon_main_color)
                
            instance.save()
            return redirect("/")

        self.ctx["form"] = form
        return render(request, "social_creation.html", self.ctx)

def social_admin(request):
    social_profiles = list(SocialProfile.objects.all())

    return render(request, "social_admin.html", {"social_profiles": social_profiles})
    
def temp_dash(request):
    return render(request, "temp_dash.html")
