from django import forms

from social.models import SocialProfile

class SocialCreationForm(forms.ModelForm):
    social_name = forms.CharField(
        label="Profile name",
        widget=forms.TextInput(
            attrs= {
                "placeholder": "Profile name",
                "class": "forms-input"
            }
        )
    )
    social_icon = forms.URLField(
        label="Icon url",
        widget=forms.URLInput(
            attrs= {
                "placeholder": "Icon url",
                "class": "forms-input"
            }
        )
    )
    social_link = forms.URLField(
        label="Profile url",
        widget=forms.URLInput(
            attrs= {
                "placeholder": "Profile url",
                "class": "forms-input"
            }
        )
    )



    class Meta:
        model = SocialProfile
        fields = ("social_name", "social_icon", "social_link")

    # def clean(self):
    #     cleaned_data = super().clean()
    #     icon_link = cleaned_data.get("social_icon")

    #     possible_extension = (".jpg", ".png", ".svg")

    #     if not str(icon_link).endswith(possible_extension):
    #         self.add_error(
    #             "social_icon",
    #             forms.ValidationError("Not a valid type, must be JPG, PNG or SVG.")
    #         )
    
    def clean_social_icon(self):
        data = self.cleaned_data["social_icon"]

        possible_extension = (".jpg", ".png", ".svg")

        if not str(data).endswith(possible_extension):
            raise forms.ValidationError("Not a valid type, must be JPG, PNG or SVG.")

        return data