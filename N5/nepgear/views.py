from django.forms import forms
from django.shortcuts import redirect, render
from django.views import View
from .forms import SocialCreationForm

# Create your views here.
class SocialCreationView(View):
    ctx = {
        "form": SocialCreationForm(),
    }

    def get(self, request, *args, **kwargs):
        
        return render(request, "social_creation.html", self.ctx)

    def post(self, request, *args, **kwargs):
        
        form = SocialCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("index")
        
        return render(request, "social_creation.html", self.ctx)
        



    