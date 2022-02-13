from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.utils.decorators import method_decorator
import json
from django.contrib.admin.views.decorators import staff_member_required

from NPG.helpers import ajax_required
from .forms import SocialCreationForm
from social.models import SocialProfile

# Create your views here.

@staff_member_required
def dashboard(request):
    return render(request, "npg_base.n5t")

@method_decorator(ajax_required, name="get")
class SocialCreationView(View):
    ctx = {
        "form": SocialCreationForm(),
    }

    def get(self, request, *args, **kwargs):
        
        return render(request, "social_creation.n5t", self.ctx)

    def post(self, request, *args, **kwargs):
        payload = json.loads(request.body.decode())
        form = SocialCreationForm(payload)
        
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({"status" : "sucess"}), status=200)

        errors = form.errors
        self.ctx["form"] = form
        return HttpResponse(json.dumps(errors), status=400)

@staff_member_required
def social_admin(request):
    social_profiles = list(SocialProfile.objects.all())

    return render(request, "social_admin.n5t", {"social_profiles": social_profiles})

@staff_member_required
def social_delete(request, card):
    object = get_object_or_404(SocialProfile, id=card)

    if request.method == "DELETE":
        object.delete()
        return HttpResponse(json.dumps({"status" : "sucess"}), status=200)
    return HttpResponse(json.dumps({"status":"failure"}), status=400)

