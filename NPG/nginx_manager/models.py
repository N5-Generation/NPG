from django.db import models
# Create your models here.

class ManagerConfig(models.Model):
    server_listen_port = models.PositiveIntegerField()
    server_name = models.TextField()
    location_root = models.TextField()
    location_index = models.TextField()


