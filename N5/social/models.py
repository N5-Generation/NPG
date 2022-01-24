from django.db import models

# Create your models here.
class SocialProfile(models.Model):
    social_name = models.CharField(default="Unnamed social profile", max_length=100)
    social_username = models.CharField(default="Unknow username", max_length=16)
    social_icon = models.CharField(default="path/to/social/icon", max_length=250)
    social_link = models.CharField(default="https://social.nepmia.fr/", max_length=100)
    social_color = models.CharField(max_length=10)
