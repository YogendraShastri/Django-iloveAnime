from django.contrib import admin
from .models import Service, Notification

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    service_list = ('service_icon', 'service_title', 'service_desc')

admin.site.register(Service, ServiceAdmin)

class NotificationAdmin(admin.ModelAdmin):
    notification_list = ('Notification_icon', 'Notification_title', 'Notification_desc')

admin.site.register(Notification, NotificationAdmin)



