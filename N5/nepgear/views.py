from django.shortcuts import redirect, render
from django.views import View
from django.utils.decorators import method_decorator
import json

from NPG.helpers import ajax_required
from .forms import SocialCreationForm
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
            form.save()
            return redirect("/")

        self.ctx["form"] = form
        return render(request, "social_creation.html", self.ctx)

def social_admin(request):
    social_profiles = list(SocialProfile.objects.all())

    return render(request, "social_admin.html", {"nik": social_profiles})
    