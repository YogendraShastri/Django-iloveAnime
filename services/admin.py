from django.contrib import admin
from .models import Service, Notification, NotesModel, VideosModel

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    service_list = ('service_icon', 'service_title', 'service_desc')

admin.site.register(Service, ServiceAdmin)

class NotificationAdmin(admin.ModelAdmin):
    notification_list = ('Notification_icon', 'Notification_title', 'Notification_desc')

admin.site.register(Notification, NotificationAdmin)

class NotesModelAdmin(admin.ModelAdmin):
    notes_list = ('Notes_image', 'Notes_title', 'Notes_desc', 'Notes_Download_link')

admin.site.register(NotesModel, NotesModelAdmin)

class VideosModelsAdmin(admin.ModelAdmin):
    video_list = ('video_title', 'video_link', 'banner_image', 'video_desc', 'video_slug')

admin.site.register(VideosModel, VideosModelsAdmin)


