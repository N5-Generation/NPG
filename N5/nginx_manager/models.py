from django.db import models
from django.utils.safestring import mark_safe 
# Create your models here.

class ManagerConfig(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    server_config_name = models.TextField(default="Untilted config")
    server_listen_port = models.PositiveIntegerField()
    server_name = models.TextField()
    location_root = models.TextField()
    location_index = models.TextField()

    def __str__(self):
        return mark_safe(("<img src='https://img.icons8.com/wired/512/server.png' width='20' height='20'>"+ self.server_config_name))


