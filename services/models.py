from django.db import models

# Create your models here.
class Service(models.Model):
    service_icon = models.CharField(max_length=60)
    service_title = models.CharField(max_length=100)
    service_desc = models.TextField()

class Notification(models.Model):
    Notification_icon = models.CharField(max_length=60)
    Notification_title = models.CharField(max_length=100)
    Notification_desc = models.CharField(max_length=100)

