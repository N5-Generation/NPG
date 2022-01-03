from django.db import models
from django.utils import timezone 
# Create your models here.

class ManagerConfig(models.Model):
    server_config_name = models.TextField(default="Untilted config [" + str(timezone.now) +"]")
    server_listen_port = models.PositiveIntegerField()
    server_name = models.TextField()
    location_root = models.TextField()
    location_index = models.TextField()

    def __str__(self):
        return self.server_config_name


