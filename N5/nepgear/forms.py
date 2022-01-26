from sys import path
from django import forms
import requests
import os
from pathlib import Path


from NPG.settings.base import STATICFILES_DIRS
from NPG.helpers import get_colors
from social.models import SocialProfile

possible_extension = (".jpg", ".png", ".svg")

class SocialCreationForm(forms.ModelForm):
    social_file = forms.FileField(
        label="",
        label_suffix="",
    )
    social_name = forms.CharField(
        label="Profile name",
        label_suffix= "",
        widget=forms.TextInput(
            attrs= {
                "placeholder": "Profile name",
                "class": "n5-input onlydark_mid-bg onlydark_mid-h-bg uR"
            }
        )
    )
    social_username = forms.CharField(
        label="Username/Tag",
        label_suffix= "",
        widget=forms.TextInput(
            attrs= {
                "placeholder": "Username/Tag",
                "class": "n5-input onlydark_mid-bg onlydark_mid-h-bg uR"
            }
        )
    )
    social_icon = forms.URLField(
        label="Icon url",
        label_suffix= "",
        widget=forms.URLInput(
            attrs= {
                "placeholder": "Icon url",
                "class": "n5-input onlydark_mid-bg onlydark_mid-h-bg uR"
            }
        )
    )
    social_link = forms.URLField(
        label="Profile url",
        label_suffix= "",
        widget=forms.URLInput(
            attrs= {
                "placeholder": "Profile url",
                "class": "n5-input onlydark_mid-bg onlydark_mid-h-bg uR"
            }
        )
    )
    social_color = forms.CharField(
        label="",
        label_suffix= "",
        widget=forms.HiddenInput(),
        required=False
    )

    class Meta:
        model = SocialProfile
        fields = ("social_name", "social_username", "social_icon", "social_link", "social_color")

    def clean(self):
        cleaned_data = super().clean()
        icon_link = cleaned_data.get("social_icon")

        if not str(icon_link).endswith(possible_extension):
            self.add_error(
                "social_icon",
                forms.ValidationError("Not a valid type, must be JPG, PNG or SVG.")
            )
            self.add_error(None, "ERROR")

    def save(self, commit = True):
        form = super().save(commit)

        # Quick binds
        social_name = self.cleaned_data["social_name"]
        social_icon = self.cleaned_data["social_icon"]
        file_extension = None

        for extension in possible_extension:
            if extension in social_icon:
                file_extension = extension 

        downloaded_icon = requests.get(social_icon).content
        icon_save_path = Path.joinpath(STATICFILES_DIRS[0],"social_icons" , f"social_{social_name}{file_extension}")

        if os.path.exists(icon_save_path):
            os.mkdir(Path.joinpath(STATICFILES_DIRS[0],"social_icons"))

        with open(icon_save_path, "wb") as save_icon:
            save_icon.write(downloaded_icon)
        
        if icon_main_color := get_colors(icon_save_path)[0]:
            rgba_final_color = "rgba" + str(icon_main_color + (.35,))
            form.social_color = rgba_final_color
            form.social_icon = f"/static/social_icons/social_{social_name}{file_extension}"

        if commit:
            form.save()
        return form