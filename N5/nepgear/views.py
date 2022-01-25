from django.http import HttpResponse
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

        errors = form.errors
        self.ctx["form"] = form
        return HttpResponse(json.dumps(errors))

def social_admin(request):
    social_profiles = list(SocialProfile.objects.all())

    return render(request, "social_admin.html", {"social_profiles": social_profiles})
    
def temp_dash(request):
    return render(request, "temp_dash.html")
