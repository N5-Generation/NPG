from django import forms

from social.models import SocialProfile

possible_extension = (".jpg", ".png", ".svg")

class SocialCreationForm(forms.ModelForm):
    social_name = forms.CharField(
        label="Profile name",
        label_suffix= "",
        widget=forms.TextInput(
            attrs= {
                "placeholder": "Profile name",
                "class": "n5-input"
            }
        )
    )
    social_username = forms.CharField(
        label="Username/Tag",
        label_suffix= "",
        widget=forms.TextInput(
            attrs= {
                "placeholder": "Username/Tag",
                "class": "n5-input"
            }
        )
    )
    social_icon = forms.URLField(
        label="Icon url",
        label_suffix= "",
        widget=forms.URLInput(
            attrs= {
                "placeholder": "Icon url",
                "class": "n5-input"
            }
        )
    )
    social_link = forms.URLField(
        label="Profile url",
        label_suffix= "",
        widget=forms.URLInput(
            attrs= {
                "placeholder": "Profile url",
                "class": "n5-input"
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
