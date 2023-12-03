from pyexpat import model
from statistics import mode
from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Service(models.Model):
    service_icon = models.FileField(upload_to='images/',max_length=300,null=False,default=None)
    service_title = models.CharField(max_length=200)
    service_slug = AutoSlugField(populate_from='service_title',unique=True,null=True,default=None)
    service_desc = models.TextField()
    service_detailed_desc = models.TextField(null=True, default='')

class Notification(models.Model):
    Notification_icon = models.CharField(max_length=60)
    Notification_title = models.CharField(max_length=200)
    Notification_slug = AutoSlugField(populate_from='Notification_title',unique=True,null=True,default=None)
    Notification_desc = models.CharField(max_length=200)
    Notice_link = models.URLField(default='', null=True)

class NotesModel(models.Model):
    Notes_image = models.FileField(upload_to='images/',max_length=300,null=False,default=None)
    Notes_title = models.CharField(max_length=200)
    Notes_desc = models.TextField()
    Notes_Download_link = models.URLField(null=False)

class VideosModel(models.Model):
    video_title = models.CharField(max_length=255)
    video_link = models.URLField()
    banner_image = models.ImageField(upload_to='youtube_banners/')
    video_desc = models.TextField()
    video_slug = AutoSlugField(populate_from='video_title',unique=True,null=True,default=None)



